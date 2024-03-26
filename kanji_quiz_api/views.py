from rest_framework import generics, permissions
from .models import KanjiQuiz
from .serializers import KanjiQuizSerializer


class KanjiQuizListView(generics.ListAPIView):
    queryset = KanjiQuiz.objects.all()
    serializer_class = KanjiQuizSerializer
    http_method_names = ["get"]


class KanjiQuizCreateView(generics.CreateAPIView):
    queryset = KanjiQuiz.objects.all()
    serializer_class = KanjiQuizSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']
    