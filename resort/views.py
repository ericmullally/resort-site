from django.shortcuts import render

def index(request):
    return render(request, "resort/index.html")

def booking(request):
    pass

def ammenities(request , slug):
    pass