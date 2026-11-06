from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    firstname = models.CharField(max_length=100,null=False)
    lastname = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,null=False,unique=True)
    password = models.CharField(max_length=100,null=False)
    mobileno = models.BigIntegerField(null=False,unique=True)
    location = models.CharField(max_length=100)
    zipcode = models.BigIntegerField(null=False)

    class Meta:
            db_table = 'data_employee'
            ordering = ["firstname"]