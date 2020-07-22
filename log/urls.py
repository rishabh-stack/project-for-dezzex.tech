from django.urls import path
from.import views



urlpatterns = [
   
    path('', views.index,name='loghome'),
    path('signup', views.handleSignup, name='handlesignup'),
    path('login', views.handlelogIn, name='handlelogin'),
    path('logout', views.handlelogOut, name='handlelogout'),
]

