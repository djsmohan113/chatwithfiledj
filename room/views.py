from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import roomRoomForm
from .models import *


@login_required
def rooms(request):
    rooms = roomRoomModel.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = roomRoomForm(request.POST)
        if form.is_valid():
            room = form.save()  # Save the room instance
            return redirect(rooms)  # Redirect to the rooms list page
    else:
        form = roomRoomForm()

    return render(request, 'room/create_room.html', {'form': form})


# @login_required
# def delete_room(request, id):
#     try:
#         room = roomRoomModel.objects.get(id=id)
#     except:
#         raise Http404("Room does not exist")  # Raise Http404 exception if the room doesn't exist
#
#     room.delete()
#     return redirect(rooms)



@login_required
def room(request, id):
    room = roomRoomModel.objects.get(id=id)
    messages = roomMessageModel.objects.filter(room=room)

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
