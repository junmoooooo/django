from django.db import models

# Create your models here.
# 생각한 속성을 바탕으로 질문(Question)과 답변(Answer)에 
# 해당되는 모델을 pybo/models.py 파일에 정의해 보자.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

#Answer 모델은 질문에 대한 답변에 해당되므로 Question 모델을 속성으로 가져가야 한다. 