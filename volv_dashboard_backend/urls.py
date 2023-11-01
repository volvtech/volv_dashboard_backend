"""
URL configuration for volv_dashboard_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# from volv_dashboard_backend.volv_dashboard import views

from volv_dashboard_backend.volv_dashboard.views import ArticlesListView, ArticleView, ArticleCreateView, UserLoginView, \
    ArticlesFiltersView, PublisherView

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'model', views.ArticleCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^api-token-auth/', obtain_jwt_token),
    # path(r'^api-token-refresh/', refresh_jwt_token),
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/<int:page_id>', ArticlesListView.as_view(), name='Get list of articles'),
    path('articles_filters/', ArticlesFiltersView.as_view(), name='Get list of filter options'),
    path('article/<int:article_id>', ArticleView.as_view(), name='Get an Article Detail'),
<<<<<<< HEAD
    path('articles/create/', ArticleCreateView.as_view(), name='Create an Article'),
=======
>>>>>>> bde6dbd (publishers API)
    path('publishers/', PublisherView.as_view(), name='List of Publishers'),
]

admin.site.site_header = "Volv Admin"
admin.site.site_title = "Volv Admin Portal"
admin.site.index_title = "Welcome to Volv Portal"