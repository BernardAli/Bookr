from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    name = "world"
    return render(request, 'home.html', {"name": name})


