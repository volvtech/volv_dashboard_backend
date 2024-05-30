from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.db.models import Q

from volv_dashboard_backend.volv_dashboard.models import Articles, Publishers, Authors, Users, ArticleStatuses, ArticleCategories, ArticleHashtags, CheckItOutOptions, ArticlePublishTimes
from volv_dashboard_backend.volv_dashboard.permissions import StaffPermission, HasAPIKey
from volv_dashboard_backend.volv_dashboard.serializers import ArticlesListSerializer, ArticleDetailSerializer, \
    UserLoginSerializer
import operator
from functools import reduce

from volv_dashboard_backend.log_conf import Logger

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from volv_dashboard_backend.volv_dashboard.utils import generate_token, send_reset_email

LOGGER = Logger.get_logger(__name__)


class ArticlesListView(APIView):
    # permission_classes = [StaffPermission | HasAPIKey]
    permission_classes = []

    def get_filtered_articles(self, request_data):
        """This function will filter and send articles"""
        LOGGER.info(f"#volv_dashboard #views #ArticlesListView #get_filtered_articles request_data====> {request_data}")

        search_term = request_data.get('search_term', "")
        LOGGER.info(f"#volv_dashboard #views #ArticlesListView #get_filtered_articles search_term====> {search_term}")
        search_term_condition = []
        if search_term:
            request_data.pop("search_term")
            search_term_condition = [Q(article_author__icontains=search_term) |
                        Q(article_heading__icontains=search_term) |
                        Q(article_summary__icontains=search_term) |
                        Q(article_status__icontains=search_term) |
                        Q(article_category__icontains=search_term)]

        all_conditions = ([Q(**{filter_item:request_data[filter_item]}) for filter_item in request_data] +
                          search_term_condition)
        conditions = reduce(operator.and_, all_conditions)
        LOGGER.info(f"#volv_dashboard #views #ArticlesListView #get_filtered_articles conditions====> {conditions}")
        all_articles = (Articles.objects.filter(conditions).order_by('-updated_at'))
        return all_articles

    def post(self, request, page_id):
        try:
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views POST request_data: {request.data}")
            request_data = request.data
            all_articles = self.get_filtered_articles(request_data)
            paginated_articles = Paginator(all_articles, per_page=10)
            articles = paginated_articles.get_page(page_id)
            articles_serializer = ArticlesListSerializer(articles, many=True)
            return JsonResponse({'data': articles_serializer.data, 'total_pages': paginated_articles.num_pages})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views GET #ERROR: {str(err)}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleView(APIView):
    # permission_classes = [StaffPermission | HasAPIKey]
    permission_classes = []

    def get_article_obj(self, article_id):
        LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView get_article_obj article_id:"
                     f" {article_id}")
        article_obj = None
        try:
            article_obj = Articles.objects.get(id=article_id)
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView get_article_obj ERROR:"
                          f" {str(err)}")
        return article_obj

    def post(self, request, article_id):
        try:
            LOGGER.info("#volv_dashboard_backend #volv_dashboard #views #ArticleView POST Starts...")
            article = self.get_article_obj(article_id)
            if article:
                article_serializer = ArticleDetailSerializer(article)
                article_details = article_serializer.data
                LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView article_details: "
                             f"{article_details}")
                return Response(status=status.HTTP_200_OK, data={'article': article_details})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Article Does Not Exists'})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView POST #ERROR: {str(err)}",
                          exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, article_id):
        try:
            LOGGER.info("#volv_dashboard_backend #volv_dashboard #views #ArticleView PATCH Starts...")
            article = self.get_article_obj(article_id)
            if article:
                article_serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
                if article_serializer.is_valid():
                    article_serializer.save()
                    article_details = article_serializer.data
                    LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView article_details: "
                                f"{article_details}")
                    return Response(status=status.HTTP_200_OK, data={'article': article_details})
                LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView article_details article_id: {article_id} #ERROR: ArticleDetailSerializer is invalid")
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Rquest is invalid"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Article Does Not Exists'})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView PATCH #ERROR: {str(err)}",
                          exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, article_id):
        try:
            LOGGER.info("#volv_dashboard_backend #volv_dashboard #views #ArticleView DELETE Starts...")
            article = self.get_article_obj(article_id)
            if article:
                article.delete()
                LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView DELETE article {article_id} is deleted")
                return Response(status=status.HTTP_200_OK, data={'message': "Article Deleted Successfully"})
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView DELETE article {article_id} DOES NOT EXISTS")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': "Article Does Not Exists"})
        except Exception as err:
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView DELETE article {article_id} ERROR: {str(err)}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'message': "Internal Server Error"})

class ArticleCreateView(APIView):
    permission_classes = ()

    def save_article_publish_time(self, article_id, article_publish_time):
        try:
            if article_id:
                from datetime import datetime
                date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ArticlePublishTimes.objects.create(article_id=article_id,
                                                article_publish_time=article_publish_time,
                                                created_at=date_now,
                                                updated_at=date_now
                                                )
                LOGGER.info(f"ArticleCreateView #save_article_publish_time Article Publish Time saved for article_id: {article_id}")

        except Exception as err:
            LOGGER.error(f"ArticleCreateView #save_article_publish_time #ERROR: {str(err)}")

    def post(self, request):
        try:
            print(f"STARTTTTT....")
            print(f"request {request.data}....")
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleCreateView POST User: {request.user}"
                         f"data: {request.data}")
            article_serializer = ArticleDetailSerializer(data=request.data)
            if article_serializer.is_valid():
                article_serializer.save()
                if article_serializer.data:
                    article_id = article_serializer.data.get('id', None)
                    article_publish_time = request.data.get('article_publish_time', None)
                    self.save_article_publish_time(article_id=article_id, article_publish_time=article_publish_time)
                    return Response(article_serializer.data, status.HTTP_201_CREATED)
            else:
                return Response({'error': article_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleCreateView GET #ERROR: "
                          f"{str(err)}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(APIView):
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permissions
    def post(self, request):
        print(f"data: {request.data}")
        user_serializer = UserLoginSerializer(data=request.data)
        print(f"valid: {user_serializer.is_valid()}")
        if user_serializer.is_valid():
            user = user_serializer.validated_data
            # print(f"user_email: {user.id}")
            data = user_serializer.data
            # data = Users.objects.get(id=user.id)
            # print(f"data: {data}")
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            # Generate JWT token
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return Response({'token': token, "data": data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ArticlesFiltersView(APIView):
    # permission_classes = [StaffPermission | HasAPIKey]
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permissions

    def post(self, request):
        try:
            request_data = request.data
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticlesFiltersView #GET starts... request_data: {request_data}")
            article_publisher_filter_options = Publishers.objects.all().values_list('id', 'publisher_title')
            article_author_filter_options = Users.objects.all().values_list('id', 'name')
            article_status_filter_options = ArticleStatuses.objects.all().values_list('id', 'status')
            article_category_filter_options = ArticleCategories.objects.all().values_list('id', 'category_title')
            check_it_out_filter_options = CheckItOutOptions.objects.all().values_list('id', 'option')

            filter_options = {
                "publisher_filters": article_publisher_filter_options,
                "author_filters": article_author_filter_options,
                "status_filters": article_status_filter_options,
                "category_filters": article_category_filter_options,
                "check_it_out_filter_options": check_it_out_filter_options,
            }

            filter_response = {}
            for filter in filter_options:
                if filter in request_data.get("filters", None):
                    filter_response[filter] = filter_options[filter]

            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticlesFiltersView filter_response: "
                        f"{filter_response}")

            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticlesFiltersView filter_options: "
                        f"{filter_options}")

            return Response(status=200, data={'data': filter_response})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticlesFiltersView #GET #ERROR: "
                         f"{str(err)}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PublisherView(APIView):
    # permission_classes = [StaffPermission | HasAPIKey]
    permission_classes = []

    def get(self, request):
        try:
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #PublisherView #GET starts...")
            publishers = Publishers.objects.all().values_list('id', 'publisher_title')
            # publishers_data = []
            # for publisher in publishers:
            #     # publishers_data.append({"publisher_id": publisher[0], "publisher_title": publisher[1]})
            #     publishers_data.append({"publisher_id": 1, "publisher_title": 'DIpak'})

            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #PublisherView publishers: "
                        f"{publishers}")
            return Response(status=200, data={'data': publishers})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #PublisherView #GET #ERROR: "
                         f"{str(err)}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class PasswordResetView(APIView):
    permission_classes = []

    def post(self, request):
        try:
            LOGGER.info(f"#views #PasswordResetView #POST starts...")
            print(f"#views #PasswordResetView #POST data: {request.data}")
            password_reset_serializer = PasswordResetSerializer(data=request.data)
            print(f"#views #PasswordResetView #POST valid: {user_serializer.is_valid()}")
            if password_reset_serializer.is_valid():
                print(f"#views #PasswordResetView #POST Email is valid")

                plaintext = get_template('email.txt')
                htmly     = get_template('email.html')

                d = Context({ 'username': username })

                subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
                text_content = plaintext.render(d)
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': password_reset_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            LOGGER.error(f"#views #PasswordResetView #POST #ERROR: {str(err)}")


class HashtagsView(APIView):
    permission_classes = []

    # permission_classes = [StaffPermission | HasAPIKey]
    def post(self, request):
        try:
            LOGGER.info("#volv_dashboard_backend #volv_dashboard #views #HashtagsView GET Starts...")
            article_hashtags = ArticleHashtags.objects.all().values_list('id', 'category_ids', 'sub_category')
            LOGGER.info(f"#volv_dashboard_backend #volv_dashboard #views #HashtagsView article_hashtags: "
                            f"{article_hashtags}")
            return Response(status=status.HTTP_200_OK, data={'article_hashtags': article_hashtags})
        except Exception as err:
            LOGGER.error(f"#volv_dashboard_backend #volv_dashboard #views #HashtagsView GET #ERROR: {str(err)}",
                          exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class ForgotPasswordView(APIView):
    permission_classes = ()
    def get_queryset(self):
        return Users.objects.all()

    def post(self, request):
        try:
            email = request.data.get('email')
            user = Users.objects.get(email=email)
            LOGGER.info(f"USER**: {user.id}")
            if user:
                # token = default_token_generator.make_token(user)
                random_token = generate_token()
                Users.objects.filter(id=user.id).update(token=random_token)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = f"http://example.com/reset-password/?uid={uid}&token={random_token}"
                send_reset_email(email, reset_link)
                # Send email with reset link containing uid and token
                # Example: http://example.com/reset-password/?uid=<uid>&token=<token>
                # You can use Django's built-in EmailMessage to send emails
                return Response({'message': 'Reset link sent to your email'}, status=status.HTTP_200_OK)
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            LOGGER.error(f"#views.py #ForgotPasswordView #ERROR: {str(err)}", exc_info=True)
            return Response({'error': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

class ResetPasswordView(APIView):
    def post(self, request):
        try:
            uidb64 = request.data.get('uid')
            token = request.data.get('token')
            password = request.data.get('password')
            
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Users.objects.get(pk=uid)
            
            # if user and default_token_generator.check_token(user, token):
            if user and user.token == token:
                user.set_password(password)
                user.save()
                return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            LOGGER.error(f"#views.py #ResetPasswordView #ERROR: {str(err)}", exc_info=True)
            return Response({'error': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
