import datetime
from xmlrpc.client import boolean

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    def __str__(self): # 객체의 표현을 대화식 프롬프트에서 편하게 보려는 이유 말고도, \
        # Django가 자동으로 생성하는 관리 사이트에서도 객체의 표현이 사용되기 때문
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    