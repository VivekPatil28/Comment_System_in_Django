from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'signin.html')
    comments = Comment.objects.filter(parent=None)
    params={
        'comments':comments,
    }
    return render(request,'index.html',params)


def submitcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        comment_id = request.POST['reply_to']
        user = request.user
        print(comment, comment_id, user)
        if comment_id:
            parent = Comment.objects.get(id=comment_id)
            Comment.objects.create(content=comment, parent=parent, user=user)
        else:
            Comment.objects.create(content=comment, parent=None, user=user)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            index(request)

def signout(request):
    logout(request)
    return render(request,'signin.html')
        
