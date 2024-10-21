from django.urls import path
from .views import UserDetaillView, UserCreateView, UserDeleteView, UserUpdateView

urlpatterns = [
  path('users/<int:pk>/', UserDetaillView.as_view(), name='user-detail'),
  path('users/', UserCreateView.as_view(), name='user-create'),
  path('users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
  path('users/update/<int:pk>', UserUpdateView.as_view(), name='user-update')
]