from django.shortcuts import render

# Create your views here.

def index(request):
    """ Return to index page """
    
    return render(request, 'home/index.html')