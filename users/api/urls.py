from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api.views import registration_view, get_all_users

app_name = 'users'

urlpatterns = [
    # w postmanie: api/users/login
    path('login', obtain_auth_token, name='login'),

    # w postmanie: /api/users/users api/users/register
    path('register', registration_view, name='register'),
# {
# 	"username":"robcio",
# 	"email":"robcio@robcio.pl",
# 	"password":"Dupa123$%^",
# 	"confirm_password":"Dupa123$%^"
# }

    # w postmanie: /api/users/users
    path('users', get_all_users, name='users')
]
