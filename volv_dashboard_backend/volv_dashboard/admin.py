from django.contrib import admin

from volv_dashboard_backend.volv_dashboard.models import Articles, Publishers, ArticleHashtags, ArticleCategories, ArticleStatuses, CheckItOutOptions


# Register your models here.

# @admin.register(Articles)
# class ArticlesAdmin(admin.ModelAdmin):
#     fields = '__all__'


admin.site.register(Articles)
admin.site.register(Publishers)
admin.site.register(ArticleHashtags)
admin.site.register(ArticleCategories)
admin.site.register(ArticleStatuses)
admin.site.register(CheckItOutOptions)
