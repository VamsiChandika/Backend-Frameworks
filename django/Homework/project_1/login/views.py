from django.shortcuts import render,redirect
from view.models import Student
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        result = Student.objects.filter(email=email,password=password)
        if result.exists():
            student = result.first()

            request.session["student_id"] = student.id
            request.session["email"] = student.email
           
            return redirect('dashboard')
        else:
            messages.error(
                request,
                "Invalid Username or Password"
            )
            return redirect('login')
        
    return render(request,'login.html')