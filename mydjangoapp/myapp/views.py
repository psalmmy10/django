from django.shortcuts import render
# from django.http import  HttpResponse
from .models import Blog , About


# Create your views here.
def index (request):
    posts = Blog.objects.all() 
    return render (request, 'index.html',{'posts' : posts})

def blogPosts(request,pk):
    Posts = Blog.objects.get(id = pk)
    return render (request,'blogPost.html', {'Posts':Posts})  

# def about (request,pk):
#     text =  About.objects.get(id = pk)
#     return render (request, 'about.html', {'text': text})