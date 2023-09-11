from rest_framework import serializers
from volv_dashboard_backend.volv_dashboard.models import Articles


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'article_heading', 'article_summary', 'article_author', 'article_category', 'article_image']
        many = True


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
