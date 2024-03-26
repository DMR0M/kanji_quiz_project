from django.db import models
from django.utils import timezone


class KanjiQuiz(models.Model):
    kanji_character = models.CharField(max_length=100)
    hiragana_character = models.CharField(max_length=300)
    reading = models.CharField(max_length=300)
    meaning = models.CharField(max_length=300)
    
    def __str__(self):
        return self.kanji_character
    
    
class QuizScores(models.Model):
    total_score = models.IntegerField()
    question_count = models.IntegerField()
    data_answered = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"Total Score: {self.total_score}/{self.question_count}"
    
    