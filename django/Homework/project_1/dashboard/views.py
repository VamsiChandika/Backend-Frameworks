from django.shortcuts import render,redirect
from view.models import Student
# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    request.session.delete()
    return redirect('login')
