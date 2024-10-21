from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UserView(APIView):
  def get(self, request, pk): 
    try:
      user_data = User.objects.get(id=pk)
      serializer = UserSerializer(user_data, context={ 'request': request })
      return Response(serializer.data)
    except:
      return Response({ "Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)