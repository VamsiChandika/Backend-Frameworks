from django.shortcuts import render,redirect
from data.models import Employee
# Create your views here.
def data(request):
    request.session
    if "firstname" in request.session:
        result = Employee.objects.all() # select * from employee
        return render(request,'data.html',{'employee' : result})
    else:
        return redirect('/login/?next=/data/')
    
    
    
        