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
    all_users = User.ojects.exclude
    (id=request.user.id)
    liked_posts = [i for i in Post.objects.all() if Like.objects.filter(user = request.user, post=i)]

# Create your views here.
