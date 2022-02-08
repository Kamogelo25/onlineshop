#create this file to register all the apps url. 
#If we registered them in the projects url it would be too long and messy
from .views import *
from django.urls import path


app_name = 'shop'

urlpatterns = [
    path('', HomePageView, name = 'home'), #empty string represents the home page. name is what we use to create the url({% url:'home' %})
]