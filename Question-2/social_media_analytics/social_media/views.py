from django.shortcuts import render

def user(request):
    
    return render(request, 'topuser.html')

def post(request):
    return render(request, 'toppost.html')

def feed(request):
    return render(request, 'topfeed.html')

# Create your views here.
