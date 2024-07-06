from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("home index")
    return render(request, "home/index.html")
