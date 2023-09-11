from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from volv_dashboard_backend.volv_dashboard.models import Articles
from volv_dashboard_backend.volv_dashboard.permissions import StaffPermission, HasAPIKey
from volv_dashboard_backend.volv_dashboard.serializers import ArticlesListSerializer, ArticleDetailSerializer

import logging


class ArticlesListView(APIView):
    permission_classes = [StaffPermission | HasAPIKey]
    def get(self, request):
        try:
            logging.info("#volv_dashboard_backend #volv_dashboard #views GET Starts...")
            all_articles = Articles.objects.all().order_by('-updated_at')
            paginated_articles = Paginator(all_articles, per_page=10)  # Adjust per_page as needed
            articles = paginated_articles.get_page(1)
            articles_serializer = ArticlesListSerializer(articles, many=True)
            return JsonResponse({'data': articles_serializer.data, 'total_pages': paginated_articles.num_pages})
        except Exception as err:
            logging.error(f"#volv_dashboard_backend #volv_dashboard #views GET #ERROR: {str(err)}", exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleView(APIView):
    permission_classes = [StaffPermission | HasAPIKey]

    def get_article_obj(self, article_id):
        logging.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView get_article_obj article_id:"
                     f" {article_id}")
        article_obj = None
        try:
            article_obj = Articles.objects.get(id=article_id)
        except Exception as err:
            logging.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView get_article_obj ERROR:"
                          f" {str(err)}")
        return article_obj

    def get(self, request, article_id):
        try:
            logging.info("#volv_dashboard_backend #volv_dashboard #views #ArticleView GET Starts...")
            article = self.get_article_obj(article_id)
            if article:
                article_serializer = ArticleDetailSerializer(article)
                article_details = article_serializer.data
                logging.info(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView article_details: "
                             f"{article_details}")
                return Response(status=status.HTTP_200_OK, data={'article': article_details})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Article Does Not Exists'})
        except Exception as err:
            logging.error(f"#volv_dashboard_backend #volv_dashboard #views #ArticleView GET #ERROR: {str(err)}",
                          exc_info=True)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
