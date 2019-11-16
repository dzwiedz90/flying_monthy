from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from users.api.serializers import RegistrationSerializer, GetAllUsersSerializer


# create user
@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = user.username
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


# get all users data
@api_view(['GET', ])
def get_all_users(request):
    if request.method == 'GET':
        serializer = GetAllUsersSerializer(data=request.data)
        users = User.objects.all()
        serializer = GetAllUsersSerializer(users, many=True)
        return Response({"user": serializer.data})


@api_view(['PUT', ])
def update_user(request):
    if request.method == 'PUT':

