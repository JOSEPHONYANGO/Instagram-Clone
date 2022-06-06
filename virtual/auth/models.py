from django.db import models
from django.contrib.auth.models import User
# from post.models import Post

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    location=models.CharField(max_length=50,blank=True,null=True)
    url=models.CharField(max_length=100,blank=True,null=True)
    profile_infor=models.TextField(max_length=150,null=True,blank=True)