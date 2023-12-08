from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

# HttpResponse는 요청에 대한 응답을 할때 사용한다. 
# 여기서는 "안녕하세요 pybo에 오신것을 환영합니다." 라는 
# 문자열을 브라우저에 출력하기 위해 사용