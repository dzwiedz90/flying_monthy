from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.api.views import registration_view, get_all_users, UpdateUser

app_name = 'users'

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('register', registration_view, name='register'),
    path('users', get_all_users, name='users'),
    path('users/<int:pk>', UpdateUser.as_view()),
]
