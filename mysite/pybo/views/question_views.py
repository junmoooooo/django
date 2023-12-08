from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user  # author 속성에 로그인 계정 저장
            # question.subject = "이걸로 채워지나?" 를 쓰면 덮어씌어진다.
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
# render 함수에 전달한 {'form': form}은 템플릿에서 질문 등록시 사용할 폼 엘리먼트를 생성할 때 쓰인다.
#request.POST를 인수로 QuestionForm을 생성할 경우에는 request.POST에 담긴 subject, content 값이 
# QuestionForm의 subject, content 속성에 자동으로 저장되어 객체가 생성된다.


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        #로그인한 사람과 글쓴이가 다르다면, 오류메시지 출력
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        # instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미이다
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
        #폼 생성시 이처럼 instance 값을 지정하면 폼의 속성 값이 instance의 값으로 채워진다. 
        # 따라서 질문을 수정하는 화면에서 제목과 내용이 채워진 채로 보일 것이다.

    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
    # 질문하기 수정하기는 질문등록하기와 폼이 동일하기때문   


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')



@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
        # voter는 여러사람을 추가할 수 있는 ManyToManyField이므로
        # question.voter.add(request.user) 처럼 add 함수를 사용하여 추천인을 추가한다.
    return redirect('pybo:detail', question_id=question.id)




