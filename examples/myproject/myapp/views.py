from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
def index(request, pk):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('myapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''