from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # 로그인 뷰는 따로 만들 필요없이 위 코드처럼 django.contrib.auth 앱의 LoginView를 사용하도록 설정했다.
    # 로그인은 common앱에 구현할거기떄문에 registion 디렉토리에 가지 않을거다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]