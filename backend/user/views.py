from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UserDetaillView(APIView):
  def get(self, request, pk): 
    try:
      user_data = User.objects.get(id=pk)
      serializer = UserSerializer(user_data, context={ 'request': request })
      return Response(serializer.data)
    except:
      return Response({ "Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserCreateView(APIView):
  def post(self, request):
    try:
      serializer = UserSerializer(data=request.data)
      
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response({ "Error": "Internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
      return Response({ "Error": "Error creating user"}, status=status.HTTP_400_BAD_REQUEST)