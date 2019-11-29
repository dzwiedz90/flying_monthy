from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from users.views import main_page_view, register, logout, profile, users_list, \
    change_user_status
from users.api.views import user_profile_rest
from posts.views import PostCreateView, MemeRestApi, GetMemesOfUser, \
    PostDetailView
from comments.views import CommentRestApi, GetCommentsOfUser, add_comment

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
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api')),
    path('post/api/memes/', MemeRestApi.as_view(), name='post/api/memes/'),
    path('post/api/user_memes/', GetMemesOfUser.as_view(), name='user_memes'),
    path('api/users/user_profile', user_profile_rest, name='user_profile'),
    path('comments/api/comments/', CommentRestApi.as_view(), name='comments/api/comments/'),
    path('comments/api/user_memes/', GetCommentsOfUser.as_view(), name='user_comments'),
    path('comments/add/<int:pk>/', add_comment, name='add_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
