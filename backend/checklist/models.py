from django.db import models
from django.contrib.auth.models import User

class Checklist(models.Model):
  id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklist")
  title = models.CharField(max_length=255)
  date_craetion = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.title} - {self.id_user.name}"

class Pergunta(models.Model):
  EVALUATION_CHOICES = [
    ('positivo', 'Positivo'),
    ('ok', 'Ok'),
    ('ruim', 'Ruim'),
  ]

  questionnaire = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name="perguntas")
  text = models.TextField()
  evaluation = models.CharField(max_length=50, choices=EVALUATION_CHOICES)
  foto = models.ImageField(upload_to="perguntas_fotos/", blank=True, null=True)

  def __str__(self):
    return f"{self.text[:30]} - {self.evaluation}"