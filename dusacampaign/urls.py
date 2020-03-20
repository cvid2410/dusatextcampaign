from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from smsgenerator import views as smsgenerator_views
from chat import views as chat_views
from authentication import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', smsgenerator_views.home, name='home'),
    path('', include('smsgenerator.urls')), 
    path('chat/', chat_views.chat, name='chat'),
    path('signup/', authentication_views.signupuser, name="signupuser"),
    path('logoutuser/', authentication_views.logoutuser, name="logoutuser"),
    path('loginuser/', authentication_views.loginuser, name="loginuser"),

]
