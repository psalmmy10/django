from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name = 'home'), #data comes from the creating front end into the checkview
    path ('checkview', views.checkview,  name='checkview'), 
    #in the checkview it confirms if the group name does not exist,
    # if it does it should'nt create a new name for the group and if it does it should create. 
    # And because we dont have a model for the user In our model db we pick the user from the created dynamic url
    # going to the room.
    path ('<str:room>/', views.room, name = 'room'), # this the room path for the dynamic url 
    path ('Send', views.Send, name = 'Send'),
    path ('getmessages/<str:room>/', views.getmessages, name = 'getmessages'),
]
