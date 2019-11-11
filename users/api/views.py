from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


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




