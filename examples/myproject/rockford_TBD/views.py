from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Room

#index is the main page
def index(request):
    #if request.method=="123":
    if 1:
        print ("request method = {}" .format(request.method))
        data = {
            'action': 'open',
            'time': '1351824120',
            'data': [48.756080,2.302038]
        }
        return JsonResponse(data)
    
    else:
        latest_room_list = Room.objects.order_by('-pub_date')[:5]
        template = loader.get_template('rockford_TBD/index.html')
        context = {
            'latest_room_list': latest_room_list,
        }
        return HttpResponse(template.render(context, request))

def detail(request, room_id):
    latest_room_list = Room.objects.order_by('-pub_date')[:5]
    template = loader.get_template('rockford_TBD/detail.html')
    context = {
        'latest_room_list': latest_room_list,
    }
    return HttpResponse(template.render(context, request))

def results(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'results.html', {'room': room})

def vote2(request, rooom_id):
    room = get_object_or_404(Room, pk=room_id)
    try:
        selected_choice = room.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the room voting form.
        return render(request, 'detail.html', {
            'room': room,
            'error_message': "You didn't select a choice.",
        })
    else:
        if request.POST['choice'] == 1:
            data = {
                'action': 'open',
                'time': '1351824120',
                'data': [48.756080,2.302038]
            }
            return JsonResponse(data)
        else:
            data = {
                'action': 'close',
                'time': '1351824120',
                'data': [48.756080,2.302038]
            }
            return JsonResponse(data)
        
@csrf_exempt
#"{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";
def close(request):
    data = {
        'action': 'close',
        'time': '1351824120',
        'data': [48.756080,2.302038]
    }
    return JsonResponse(data)

@csrf_exempt
#"{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";
def open(request):
    data = {
        'action': 'open',
        'time': '1351824120',
        'data': [48.756080,2.302038]
    }
    return JsonResponse(data)
