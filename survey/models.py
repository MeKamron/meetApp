from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text


# class Question(models.Model):
#     question_text = models.CharField(max_length=400)
#     pub_date = models.DateTimeField("date published", default=timezone.now)

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=5) <= self.pub_date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=400)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text


