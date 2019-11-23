#DO PREZENTOWANIA
----
REST FRAMEWORK URLS  
path('register/', register, name='register'),  - REGISTER USER REST
----

w postmanie: api/users/register
path('register', registration_view, name='register'), - REGISTER USER REST
{
	"username":"robcio",
	"email":"robcio@robcio.pl",
	"password":"Dupa123$%^",
	"confirm_password":"Dupa123$%^"
}


w postmanie: api/users/login
path('login', obtain_auth_token, name='login'), - LOGIN USER REST
----
----

w postmanie: /api/users/users
path('users', get_all_users, name='users'), - GET ALL USERS REST
----

w postmanie: /api/users/users/<id>
path('users/<int:pk>', UpdateUser.as_view()), - UPDATE REST
path('users/<int:pk>', UpdateUser.as_view()), - DELETE REST

#Meme rest api:
GET http://127.0.0.1:8000/post/api/user_memes/  GET ALL MEMES OF USER
musi byc zalogowany trzeba przekazac token  

GET http://127.0.0.1:8000/post/api/memes/   GET ALL MEMES  

POST http://127.0.0.1:8000/post/api/memes/   CREATEMEME
Body->form-data:
title
cover
category
author

PUT http://127.0.0.1:8000/post/api/memes/   MODIFY MEME
Body->form-data:
title
cover
category
author
id (mema)  

DELETE http://127.0.0.1:8000/post/api/memes/   DELETE MEME
musi byc zalogowany
{
    "id":1
}




