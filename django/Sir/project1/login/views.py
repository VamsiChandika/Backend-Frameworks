from django.shortcuts import render,redirect
from data.models import Employee
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        request.session["firstname"] = result.firstname
        try:
          result = Employee.objects.get(email=email,password=password)
          return redirect(request.POST.get('next') or 'dashboard')
        except Exception:
           messages.error(request,"Invalid user name or password!")
           return redirect('login')      
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')