from django.shortcuts import render,redirect
from django.http.response import Http404
from authen.models import Post, Comment, Profile, Like,Follow
from .forms import CreateUserForm,UploadImageForm, CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='login')
def index(request):

    posts = Post.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    liked_posts = [i for i in Post.objects.all() if Like.objects.filter(user = request.user, post=i)]
    followed = [i for i in User.objects.all() if Follow.objects.filter(follower = request.user, followed=i)]

    if request.method == 'POST':
        upload_form = UploadImageForm(request.POST, request.FILES)

        if upload_form.is_valid():
            upload_form.instance.user = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = UploadImageForm()

    context = {'upload_form': upload_form, 'posts':posts, 'liked_posts': liked_posts, 'all_users':all_users, 'followed': followed}

    return render(request, 'index.html',context)



# Create your views here.
