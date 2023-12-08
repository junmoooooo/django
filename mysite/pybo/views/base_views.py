from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question




def index(request):
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '')  # 검색어
    # page = request.GET.get('page', '1')은 http://localhost:8000/pybo/?page=1 
    # 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용한다. 
    # 만약 http://localhost:8000/pybo/ 처럼 page값 없이 호출된 경우에는 디폴트로 1이라는 값을 설정한다.
    question_list = Question.objects.order_by('-create_date')
    #order_by('-create_date')  create_date의 역순으로

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
            # subject__icontains=kw의 의미는 제목에 kw 문자열이 포함되었는지를 의미한다.
            # 대소문자 가리지 않고 찾아준다.
        ).distinct()

    paginator = Paginator(question_list, 10) #페이지 하나당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    # 요청된 페이지(page)에 해당되는 페이징 객체(page_obj)를 생성했다. 이렇게 하면 장고 
    # 내부적으로는 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.

    context = {'question_list' : page_obj, 'page': page, 'kw': kw} # question_list는 페이징 객체(page_obj)
    # context = {'question_list': question_list}
    # #포장작업? 키값이 넘어간다.
    # # 'question_list' 이 templates\pybo 로 넘어간다.

    return render(request, 'pybo/question_list.html', context)
    #render(요청에 대한것과, 받는 곳, 보낼거(위에서 포장한거)) 새로운 페이지 요청
    #게시판을 사용할거다.


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    #question_id 와 같이 넘어가야 질문에 대한 답변을 볼 수 있을듯