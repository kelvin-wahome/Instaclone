from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    people = Follow.objects.following(request.user)
    profile = User.objects.all()
    return render(request,'index.html',locals())
# Create your views here.
