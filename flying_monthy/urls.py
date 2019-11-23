"""flying_monthy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from users.views import main_page_view, register, logout, profile, users_list, \
    change_user_status
from posts.views import PostCreateView
from posts.views import MemeRestApi, GetMemesOfUser
from posts.views import PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', main_page_view, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('users_list/', users_list, name='users_list'),
    path('change_status/<int:pk>/', change_user_status, name='change_status'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    # path('add/', CreateMemeView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api')),
    path('post/api/memes/', MemeRestApi.as_view(), name='post/api/memes/'),
    path('post/api/user_memes/', GetMemesOfUser.as_view(), name='user_memes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
