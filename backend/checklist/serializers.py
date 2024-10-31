from rest_framework import serializers
from .models import Pergunta

class PerguntaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pergunta
    fields = ["text", "evaluation", "foto", "questionnaire_id"]