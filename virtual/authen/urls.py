from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path, include



urlpatterns = [
    path('',views.index, name='index'),
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/register_user/', views.accounts_register, name='register'),
    path('accounts/logout/',views.logout_user, name='logout'),
    path('comment/<post_id>',views.comment, name='comment'),
    path('like/<post_id>',views.like, name='like'),
    path('follow/<user_id>',views.follow, name='follow'),

    
]
