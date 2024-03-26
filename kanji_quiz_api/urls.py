from django.urls import path, include
from . import views

urlpatterns = [
    path("kanji_quiz_list/", views.KanjiQuizListView.as_view(), name="kanji_quiz_list"),
    path("kanji_quiz_list/create/", views.KanjiQuizCreateView.as_view(), name="kanji_quiz_create"),
]