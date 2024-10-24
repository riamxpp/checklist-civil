from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserModel(AbstractBaseUser):
  name = models.CharField(verbose_name="Nome", max_length=100, blank=False)
  email = models.CharField(verbose_name="Email", max_length=100, blank=False, unique=True)
  password = models.CharField(verbose_name="Senha", max_length=128, blank=False)
  birth = models.DateField(verbose_name="Data de nascimento", null=True)

  last_login = models.DateTimeField(default=timezone.now)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return self.email