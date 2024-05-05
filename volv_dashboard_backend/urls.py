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

from volv_dashboard_backend.volv_dashboard.views import ArticlesListView, ArticleView, ArticleCreateView, ForgotPasswordView, ResetPasswordView, UserLoginView, ArticlesFiltersView, PublisherView, HashtagsView

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'model', views.ArticleCreateView)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    # path(r'^api-token-auth/', obtain_jwt_token),
    # path(r'^api-token-refresh/', refresh_jwt_token),
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/<int:page_id>', ArticlesListView.as_view(), name='Get list of articles'),
    path('articles_filters/', ArticlesFiltersView.as_view(), name='Get list of filter options'),
    path('article/<int:article_id>', ArticleView.as_view(), name='Get an Article Detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='Create an Article'),
    path('publishers/', PublisherView.as_view(), name='List of Publishers'),
    path('password_reset/', PasswordResetView.as_view(), name='User Password Reset'),
    path('get_hashtags/', HashtagsView.as_view(), name='List of Hashtags'),
    path('get_hashtags/', HashtagsView.as_view(), name='List of Hashtags'),
]
 
admin.site.site_header = "Volv Admin"
admin.site.site_title = "Volv Admin Portal"
admin.site.index_title = "Welcome to Volv Portal"