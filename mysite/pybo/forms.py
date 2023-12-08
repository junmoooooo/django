from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):  #임의의 클래스 이름을 붙여 폼 작성을 해준다.
    class Meta: #오버라이딩 된 meta
        model = Question  # 사용할 모델-> 어떠한 데이터베이스 테이블을 지정할건지
        fields = ['subject', 'content']  # -> 직접입력할 부분만 지정
        # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols':1, 'background-color': 'green', 'placeholder':'질문상세를 입력해주세요.'}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  
    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        lable = {
            'content' : '답변내용',
        }

#폼은 쉽게 말해 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스이다.
#모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다. 
# Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.