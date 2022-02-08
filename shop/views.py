from django.shortcuts import render

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html') #render is a function that helps us display what we want to display, and requires you to also request
    