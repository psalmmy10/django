from django.shortcuts import render, redirect
# from django.http import HttpRequest
from .models import Room, Messages
from django.http import HttpResponse ,JsonResponse


# Create your views here.


def home (request):
  return render (request, 'home.html') 

def checkview(request):
  room = request.POST ['room_name']
  username= request.POST['username']
  
  if Room.objects.filter(name=room).exists():
      return redirect ('/' + room + '/?username=' + username)
  else:
      new_room = Room.objects.create(name=room)
      new_room.save()    
      return redirect ('/' + room + '/?username=' + username)
        
        
def room (request,room):
  username = request.GET.get('username')
  room_id = Room.objects.get(name=room)
  
  return render (request, 'room.html', {
    'username': username,
    'room_id': room_id,
    'room' : room 
  })  

def Send (request):
  message  = request.POST ['message']
  username = request.POST['username']
  room_id  = request.POST ['room_id']
  
  
  new_message = Messages.objects.create(values=message, user=username, room=room_id)
  new_message.save()
  return HttpResponse('Message sent successfully')
  
def getmessages(request,room):
    room_id = Room.objects.get(name=room)
    
    messages = Messages.objects.filter(room = room_id.id)
    return JsonResponse({'messages':list(messages.values())})
          
        
        
  