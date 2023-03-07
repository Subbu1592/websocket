from django.shortcuts import render
from . models import Message
# Create your views here.


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    username = request.GET.get('username')
    messages = Message.objects.filter(room=room_name)[0:25]
    context = {
        'room_name': room_name,
        'username': username,
        'messages': messages
    }

    return render(request, 'room.html', context)


"""

def room(request, room_name):
    return render(request, "room.html", {'room_name': room_name})"""
