from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
  email = models.CharField(verbose_name="Email", max_length=100, null=False, blank=False)