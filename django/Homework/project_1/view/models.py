from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    firstname = models.CharField(max_length=100,null=False)
    lastname = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,null=False,unique=True)
    password = models.CharField(max_length=100,null=False)
    course = models.CharField(max_length=100,null=False)
    department = models.CharField(max_length=100,null=False)
    guardian = models.CharField(max_length=100,null=False)
    contact = models.BigIntegerField(unique=True,null=False)

    class Meta:
        db_table = 'students'
        ordering = ['lastname']


    