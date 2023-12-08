from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):                       #테이블이름
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # on_delete=models.CASCADE는 계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제하라는 의미이다.
    # voter와 User가 겹치기 때문에 구분 필요! 
    subject = models.CharField(max_length=200)      #행이름 = models.어떤 타입로 작성할지(Char, tesxt)(추가속성)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # null, 빈칸 허용
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    # N:N 관계 허용, author와 User가 겹치기 때문에 구분필요!


    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')



#수정은 여기서 가능.
