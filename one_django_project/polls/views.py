from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Question, Choice

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context_dict = {}
    context_dict['latest_questions_list'] = latest_questions_list
    return render(request, 'polls/index.html', context=context_dict)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id) # shortcut
    context_dict = {}
    context_dict['question'] = question
    return render(request, 'polls/detail.html', context=context_dict)

def result(request, question_id):
    response = f'You are looking at the results of the question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    response = f'You are voting on question {question_id}'
    return HttpResponse(response)
