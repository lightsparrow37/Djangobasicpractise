from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.
def page1(request):
    return render(request, 'page1.html')

def page2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'page2.html', {'error_message': error_message})
    else:
        return render(request, 'page2.html')

def student_portal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = authenticate(request, username=username, password=password)
        if student is not None:
            login(request, student)
            return redirect('student_home')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid username or password'})
    return render(request, 'student_login.html')

@login_required
def student_home(request):
    return render(request, 'student_home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student_home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})