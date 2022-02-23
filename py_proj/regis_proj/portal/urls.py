from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    
    path('', views.home, name="home"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),

    








]