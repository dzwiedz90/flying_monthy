from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from posts.models import Post
from users.api.serializers import RegistrationSerializer, GetAllUsersSerializer, UpdateUserSerializer, GetUsersSerializer
from posts.serializers import GetAllMemesSerializer


# create user
@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
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

@api_view(['GET'])
def user_profile_rest(request):
    if request.method == 'GET':
        user = GetUsersSerializer(request.user)

        memes = Post.objects.filter(author=request.user.id)
        serializer = GetAllMemesSerializer(memes, many=True)

        return Response({'user': user.data, 'memes': serializer.data}, status=status.HTTP_200_OK)

class UpdateUser(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        request_user = request.user
        user = self.get_object(pk)
        serializer = UpdateUserSerializer(user, data=request.data)
        if request_user.id == user.id:
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User modified'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You cant change another users data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                request_user = request.user
                user = User.objects.get(pk=pk)
                if request_user.id == user.id:
                    user.delete()
                    return Response('User deleted', status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'You cant delete another user'},
                                    status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response('User not found', status=status.HTTP_404_NOT_FOUND)
