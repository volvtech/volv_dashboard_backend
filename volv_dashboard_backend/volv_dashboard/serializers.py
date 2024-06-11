from rest_framework import serializers
from volv_dashboard_backend.volv_dashboard.models import Articles
from django.contrib.auth import authenticate
from volv_dashboard_backend.volv_dashboard.models import Users

class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        many = True


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        # fields = ('article_heading')


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    user_data = serializers.SerializerMethodField()
    
    class Meta:
        model = Users
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request=data, username=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid email or password')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')
        return user

    def get_user_data(self, request):
        user_email = request.get('email')
        user = Users.objects.get(email=user_email)
        user_data_obj = {}
        user_data_obj['name'] = user.name
        user_data_obj['email'] = user.email
        user_data_obj['id'] = user.id
        user_data_obj['password'] = user.password
        user_data_obj['remember_token'] = user.remember_token
        user_data_obj['created_at'] = user.created_at
        user_data_obj['updated_at'] = user.updated_at
        user_data_obj['role'] = user.role
        return user_data_obj

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = Users
    def validate(self, data):
        email = data.get('email')
        user = User.objects.filter(email=email).exists()
        if not user:
            raise serializers.ValidationError('Invalid email')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')
        return user
