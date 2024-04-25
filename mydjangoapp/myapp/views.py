from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def index(request):
    return render (request,'index.html')

def count (request):
    texts = request.POST['test'] 
    amount = len(texts.split())
    return render (request, 'count.html',{'amounts' : amount})
    