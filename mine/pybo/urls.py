from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]


#path('', views.index) 처럼 pybo/ 가 생략된 '' 이 사용되었다. 
# 이렇게 되는 이유는 config/urls.py 파일에서 
# 이미 pybo/로 시작하는 URL이 pybo/urls.py 파일과 먼저 매핑되었기 때문이다.