from django.shortcuts import render,redirect
from view.models import Student
# Create your views here.

def view(request):
    if "student_id" not in request.session:
        return redirect("login")
    result = Student.objects.all()
    return render(request,'view.html',{'students' : result})

