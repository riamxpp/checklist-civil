from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate

from .models import UserModel 
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class UserDetaillView(APIView):
  def get(self, request, pk): 
    try:
      user_data = UserModel.objects.get(id=pk)
      serializer = UserSerializer(user_data, context={ 'request': request })
      return Response(serializer.data)
    except:
      return Response({ "Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserCreateView(APIView):
  permission_classes = []

  def post(self, request):
    try:
      password = request.data.get('password')
      if password:
        request.data['password'] = make_password(password)

      serializer = UserSerializer(data=request.data)
      
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response({ "Error": "Internal server error "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
      return Response({ "Error": "Error creating user"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(APIView):
  def delete(self, request, pk):
    try: 
      user = UserModel.objects.get(id=pk)
      if user:
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
      return Response({ "Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
class UserUpdateView(APIView):
  def put(self, request, pk):
    try:
      user = UserModel.objects.get(id=pk)
      serialize = UserSerializer(user, data=request.data, partial=True)
      
      if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
      
      return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({ "Error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
  
# class UserLoginView(APIView):
#   permission_classes = []

#   def post(self, request):
#     try:
#       email = request.data.get('email')
#       password = request.data.get('password')
      
#       try:
#         user = UserModel.objects.get(email=email)
#         print("user: ", user)
#       except:
#         return Response({"Error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
      
#       if user.check_password(password):
#       # user = authenticate(request, email=email, password=password)
#         refresh = RefreshToken.for_user(user)
#         return Response({
#           'refresh': str(refresh), 
#           'access': str(refresh.access_token)
#         }, 
#         status=status.HTTP_200_OK)

#       return Response({"Error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#     except Exception as e:
#       return Response({ "Error": "User not found", "Details": str(e)}, status=status.HTTP_404_NOT_FOUND)