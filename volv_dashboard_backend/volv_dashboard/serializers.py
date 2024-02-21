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
        # fields = ['article_heading', 'article_summary']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

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
