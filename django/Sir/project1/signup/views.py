from django.shortcuts import render,redirect,get_object_or_404

from data.models import Employee
# Create your views here.

def signup(request):
    if request.method == "POST":
      firstname = request.POST.get('firstname')
      lastname = request.POST.get('lastname')
      email = request.POST.get('email')
      password = request.POST.get('password')
      mobileno = request.POST.get('mobileno')
      location = request.POST.get('location')
      zipcode = request.POST.get('zipcode')
      Employee.objects.create(firstname = firstname,
                              lastname = lastname,
                              email = email,
                              password = password,
                              mobileno = mobileno,
                              location = location,
                              zipcode = zipcode)
      return redirect('login')
    return render(request,'signup.html')

def update(request,id):
   result = Employee.objects.get(id=id)
   if request.method == "POST":
     result.firstname = request.POST.get('firstname')
     result.lastname = request.POST.get('lastname')
     result.email = request.POST.get('email')
     result.password = request.POST.get('password')
     result.mobileno = request.POST.get('mobileno')
     result.location = request.POST.get('location')
     result.zipcode = request.POST.get('zipcode')
     result.save()
     return redirect('data')
   return render(request,'update.html',{'result' : result})

def delete(request,id):
   result = get_object_or_404(Employee,id=id)
   if result:
      result.delete()
      return redirect('data')
   return redirect('data')
