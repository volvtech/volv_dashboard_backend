from django.contrib import admin
from volv_dashboard_backend.volv_dashboard.models import Articles
# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    fields = '__all__'
