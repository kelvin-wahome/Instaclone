from django.shortcuts import render,redirect
from .models import Image,Profile,Comment,Likes
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from friendship.models import Friend, Follow, Block
from .forms import SignupForm,ImageForm,CommentForm,ProfileForm



@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    people = Follow.objects.following(request.user)
    profile = User.objects.all()
    return render(request,'index.html',locals())

@login_required(login_url='/accounts/login/')
def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        name = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=name)
        message = f"{name}"
        profiles = User.objects.all()
        people = Follow.objects.following(request.user)
        print(profiles)
        return render(request, 'search.html', {"message":message, "usernames":searched_profiles, "profiles":profiles,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})


def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_user = User.objects.get(username=current_user)
    the_comments = Comment.objects.all()
    print(the_comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_itself = form.save(commit=False)
            comment_itself.image = image
            comment_itself.commenter = request.user

            comment_itself.save()

            print(the_comments)


        return redirect(index)

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())


@login_required(login_url='/accounts/login/')
def follow(request,user_id):
    users = User.objects.get(id = user_id)
    follow = Follow.objects.add_follower(request.user,users)

    return redirect('indexpage')


@login_required(login_url='/accounts/login/')
def unfollow(request,user_id):
    users = User.objects.get(id = user_id)

    follow = Follow.objects.remove_follower(request.user,users)

    return redirect('indexpage')
