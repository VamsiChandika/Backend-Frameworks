from django.shortcuts import render,redirect,get_object_or_404
from view.models import Student
# Create your views here.

def update(request,id):
    result = Student.objects.get(id=id)
    if request.method == "POST":
        result.firstname = request.POST.get("firstname")
        result.lastname = request.POST.get("lastname")
        result.email = request.POST.get('email')
        result.password = request.POST.get("password")
        result.course = request.POST.get("course")
        result.department =request.POST.get("department")
        result.guardian = request.POST.get("guardian")
        result.contact = request.POST.get("contact")
        result.save()
        return redirect('view')
    return render(request,'update.html',{'result':result})

def delete(request,id):
    result = get_object_or_404(Student,id=id)
    if result:
        result.delete()
        return redirect('view')
    return render(request,'view.html')