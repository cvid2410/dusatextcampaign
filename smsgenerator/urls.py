from django.conf.urls import url                                                                                                                                                         
from . import views

app_name = 'smsgenerator'


urlpatterns = [ 
    url(r'smsgenerator$', views.broadcast_sms, name="default"),
]