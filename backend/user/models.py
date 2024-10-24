from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserModel(models.Model):
  name = models.CharField(verbose_name="Nome", max_length=100, blank=False)
  email = models.CharField(verbose_name="Email", max_length=100, blank=False, unique=True)
  password = models.CharField(verbose_name="Senha", max_length=128, blank=False)
  birth = models.DateField(verbose_name="Data de nascimento", null=True)