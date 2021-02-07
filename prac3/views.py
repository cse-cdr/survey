from django.shortcuts import render
from django.http import HttpResponse
from prac3.models import Question,Choice


# Create your views here.
def index(request):
    question_list =Question.objects.order_by('pub_date')
    context={'question_list':question_list}
    return HttpResponse(render(request,'prac3/index.html',context))

def detail(request,question_id):
    choice_list = Choice.objects.filter(question_id = question_id)
    question = Question.objects.get(id=question_id)

    context = {
        'choice_list': choice_list,
        'question': question
               }
    return  HttpResponse(render(request,'prac3/detail.html',context))

def vote(request,question_id):
    choice_id = request.POST['choice_id']
    choice = Choice.objects.get(id = choice_id)
    prev_vote = choice.vote
    choice.vote += 1
    choice.save()

    choice_list = Choice.objects.filter(question_id=question_id)
    question = Question.objects.get(id=question_id)
    context = {
        'choice_list': choice_list,
        'question': question
    }



    return HttpResponse(render(request, 'prac3/result.html', context))

    # context={'prev_val': prev_vote,'new_val':choice.vote,'choice_str':choice.choice_str}
    # return HttpResponse(render(request, 'prac3/vote.html',context))

