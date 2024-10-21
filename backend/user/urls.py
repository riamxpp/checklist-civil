from django.urls import path
from .views import UserDetaillView, UserCreateView, UserDeleteView

urlpatterns = [
  path('users/<int:pk>/', UserDetaillView.as_view(), name='user-detail'),
  path('users/', UserCreateView.as_view(), name='user-create'),
  path('users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
]