from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(b"Chat")

def room(request, room_name):
    return HttpResponse(room_name)
