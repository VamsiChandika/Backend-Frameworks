from django.shortcuts import render,redirect
from view.models import Student
# Create your views here.

def registration(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get('email')
        password = request.POST.get("password")
        course = request.POST.get("course")
        department =request.POST.get("department")
        guardian = request.POST.get("guardian")
        contact = request.POST.get("contact")
        Student.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,
                               course=course,department=department,guardian=guardian,contact=contact)
        return redirect('login')
        
    return render(request,'registration.html')