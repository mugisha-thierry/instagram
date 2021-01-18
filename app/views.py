from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import RedirectView
from .models import Post,Profile
from django.contrib.auth.models import User
from .forms import PostForm

# Create your views here.

# @login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    # form = PostForm(request.POST or None, files=request.FILES)      

    # if form.is_valid():
    #     post=form.save(commit=False)
    #     post.user = request.user.profile
    #     post.save()
    #     return redirect('home')
    context = {'posts':posts,}
    return render(request, 'home.html', context )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})    


def upload_image(request):
    current_user = request.user
    user_images = Profile.objects.filter(user = current_user).first()
    form = PostForm(request.POST or None, files=request.FILES)      

    if form.is_valid():
        post=form.save(commit=False)
        post.user = request.user.profile
        post.save()
        return redirect('home')

    return render(request, 'post.html', {"form": form})