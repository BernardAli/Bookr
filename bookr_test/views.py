from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def greeting_view(request):
    user = request.user
    return HttpResponse(f"Hey there, welcome {user} to Bookr!, Your one stop place to review books")