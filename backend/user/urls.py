from django.urls import path
from .views import UserView

urlpatterns = [
  path('users/<int:pk>/', UserView.as_view(), name='get_user')
]