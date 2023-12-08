"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]

#path('pybo/', include('pybo.urls'))의 의미는 pybo/로 시작하는 페이지를 요청하면 
# 이제 pybo/urls.py 파일의 매핑 정보를 읽어서 처리하라는 의미이다. 

# 따라서 이제 pybo/question/create, pybo/answer/create 등의 pybo/로 
# 시작하는 URL을 추가해야 할 때 config/urls.py 파일을 수정할 필요없이 
# pybo/urls.py 파일만 수정하면 된다.

# config/urls.py 파일에 pybo/ URL에 대한 매핑을 추가하는 것이다. 
# 장고의 urls.py 파일은 페이지 요청이 발생하면 가장 먼저 호출되는 파일로 
# URL과 뷰 함수 간의 매핑을 정의한다. 
# 뷰 함수는 views.py 파일에 정의된 함수를 말한다.

# pybo/ URL이 요청되면 views.index를 호출하라는 매핑을 urlpatterns에 추가하였다. 
# views.index는 views.py 파일의 index 함수를 의미한다.