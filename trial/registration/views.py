

# Create your views here.
from django.shortcuts import render

def registration_success(request):
    return render(request, 'registration/registration_success.html')
