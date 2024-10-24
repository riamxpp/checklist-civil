from django.urls import path
from .views import UserDetaillView, UserCreateView, UserDeleteView, UserUpdateView, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('users/<int:pk>/', UserDetaillView.as_view(), name='user-detail'),
  path('users/', UserCreateView.as_view(), name='user-create'),
  path('users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
  path('users/update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
  path('users/login', UserLoginView.as_view(), name='user-login'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]