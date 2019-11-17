#DO PREZENTOWANIA

path('admin/', admin.site.urls),  
path('accounts/', include('django.contrib.auth.urls')),
path('', main_page_view, name='home'),  - MAIN PAGE
----
REST FRAMEWORK URLS  
path('api/users/', include('users.api.urls', 'users_api')), - GET ALL USERS REST
path('register/', register, name='register'),  - REGISTER USER REST
----
w postmanie: api/users/login
path('login', obtain_auth_token, name='login'), - LOGIN USER REST
----
w postmanie: /api/users/users api/users/register
path('register', registration_view, name='register'), - REGISTER USER REST
{
	"username":"robcio",
	"email":"robcio@robcio.pl",
	"password":"Dupa123$%^",
	"confirm_password":"Dupa123$%^"
}
----
w postmanie: /api/users/users
path('users', get_all_users, name='users'), - GET ALL USERS REST
----
w postmanie: /api/users/users/<id>
path('users/<int:pk>', UpdateUser.as_view()), - UPDATE REST
path('users/<int:pk>', UpdateUser.as_view()), - DELETE REST