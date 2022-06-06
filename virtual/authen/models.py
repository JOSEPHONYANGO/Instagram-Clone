from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',null=True)
    name=models.CharField(max_length=50)
    bio=models.TextField(max_length=100,blank=True,null=True)
    profile_pic=CloudinaryField('images')
    created=models.DateField(auto_now_add=True)
    

    def _str_(self):
        return f'{self.user.username} Profile'

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs): 
        if created:
            Profile.objects.create(user=instance)  

    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_item):
        return cls.objects.filter        (user_username_icontains = search_term).all()
        def _str_(self):
            return f"{self.user.first_name}'s Profile"    

class Post(models.Model):
    image = CloudinaryField('images')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        '''
         Class method dispalays images by date
        '''
        ordering = ["-pk"]

    def save_post(self):
        '''
        Method to save our images
        '''
        self.save()

    def delete_post(self):
        '''
        Method to delete images
        ''' 
        self.delete()

    def _str_(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True) 

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete() 

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter
        (post__id=id)
        return comments 

    def _str_(self):
         return self.comment

    class Meta:
        ordering=["-pk"]             


