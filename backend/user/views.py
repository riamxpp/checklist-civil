from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_user(request): 
  return Response(UserSerializer({ 'name': "Riam", 'email': "riam@gmail.com", 'password': '1234' }))