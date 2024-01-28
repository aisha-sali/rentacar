from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 200, null=True)
    price = models.FloatField()
    year = models.CharField(max_length = 200, null=True)
    mileage = models.CharField(max_length = 200, null=True)
    trans = models.CharField(max_length = 200, null=True)  
    image = models.ImageField(null=True, blank = True)
    image1 = models.ImageField(null=True, blank = True)
    desc = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name



class Booking(models.Model):

    car = models.CharField(max_length=200, null=True, blank=True)
    customer = models.CharField(max_length=200, null=True, blank=True)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date_date = models.CharField(max_length = 200 , null = True, blank = True)
    pickup_date = models.CharField(max_length = 200 , null = True, blank = True)
    return_date = models.CharField(max_length = 200 , null = True, blank = True)
    pickup_location = models.CharField(max_length = 200 , null = True, blank = True)
    return_location = models.CharField(max_length = 200 , null = True, blank = True)
    special_request = models.CharField(max_length = 500, null=True, blank=True)
    # children = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.email

class feedback(models.Model):
    
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.TextField()
    

    def __str__(self):
        return self.email

class notification(models.Model):

    email=models.CharField(max_length=200)
    

    def __str__(self):
        return self.email

class review(models.Model):
    
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()
    

    def __str__(self):
        return self.email
    
class client(models.Model):
    
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=20)
    

    def __str__(self):
        return self.firstname