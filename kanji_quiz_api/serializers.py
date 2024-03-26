from rest_framework import serializers
from .models import KanjiQuiz


class KanjiQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanjiQuiz
        fields = "__all__"
        