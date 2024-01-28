from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout

from django import forms
from .forms import userUpdate

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *



def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Invalid Login Details!")
                return redirect('login')
            

        return render(request , 'app/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username = request.POST['username']
            email = request.POST['email']
            password=request.POST['password']
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username is Already Taken!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)  
                user.save()
            return redirect('/')
        context={}
        return render(request , 'app/signup.html', context)

@login_required(login_url='login')    
def home(request):
    
    context = {}
    return render(request, 'app/home.html', context)

@login_required(login_url='login')    
def cars(request):
    cars = Car.objects.all()

    context = {'cars': cars}
    return render(request, 'app/cars.html', context)

@login_required(login_url='login')    
def detail(request, pk):
    user=request.user
    # customers = Customer.objects.get(user__username=user.username)
    cars = Car.objects.get(id=pk)
    context = {'cars': cars, }
    user = request.user
    customer= user.username
       
    
    if request.method == "POST":
          
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = user.email
        phone = request.POST['phone']
        ploc = request.POST['plocation']
        pickup_date = request.POST['pickup_date']
        return_date = request.POST['return_date']
        rloc = request.POST['rlocation']
        sreq = request.POST['specialreq']

           
        book = Booking.objects.create(firstname =fname ,email=email,customer=customer,lastname = lname,phone=phone, car=cars.name, pickup_date = pickup_date, return_date = return_date, pickup_location = ploc, return_location = rloc, special_request = sreq)
        book.save()
        messages.success(request, 'Your booking is successful')
        return redirect('home')
       


    return render(request, 'app/form.html', context)

def logoutUser(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')    
def personal(request):
    pass
#     user=request.user
#     # cus = customer.objects.get(user=user)
#     if request.method == "POST":
        
#         user = request.user
#         n1 = request.POST['firstname']
#         n2 = request.POST['lastname']
#         email = request.POST['email']
#         phone = request.POST['number']
#         if Customer.objects.filter(user = user).exists():
#             person= Customer.objects.get(user=user)
#             person.firstname = n1
#             person.lastname=n2
#             person.email = email
#             person.phone = phone
#             person.save()
#         else:
#             person = Customer.objects.create(user = user,firstname = n1 , lastname = n2, email = email, phone = phone )
#             person.save()
        
#         return redirect('cars')
        
    
#     context={}
#     return render(request , 'app/personal.html', context)

@login_required(login_url='login')    
def booking(request):
    
    user= request.user
    customerobj = Customer.objects.get(user__username=user.username)

    booking = Booking.objects.get_or_create(name = customerobj.firstname)
    cars = Car.objects.get(name = booking.Car.name)
        
        
    context = {'cars':cars ,'booking': booking}
    return redirect('mybookings')

    return render(request, 'app/booking.html', context)

def profile(request):
    context={}
    return render(request, 'app/profile.html', context)

@login_required(login_url='login')   
def mybookings(request):
    user= request.user
    book=Booking.objects.filter(email = user.email).all()
    context = {
        'userbooking':book
        }
    return render(request, 'app/mybookings.html', context)

def cancelf(request,id):
  
    items=Booking.objects.get(id=id)
    items.delete()

    user= request.user
    book=Booking.objects.filter(email = user.email).all()
    context = {
        'userbooking':book
        }
    return render(request, 'app/mybookings.html', context)


@login_required(login_url='login')   
def fdback(request):
    if request.method == 'POST':
        
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        
        f = feedback.objects.create(name=name,phone=phone,email=email,message=message)
        print(f)
        f.save()
      
        return redirect("home")

    return render(request,"home.html")

def notify(request):

    if request.method == 'POST':
        
        email=request.POST['email']
        
        n = notification.objects.create(email=email)
        print(n)
        n.save()
      
        return redirect("home")

def Review(request):

    if request.method == 'POST':

        name=request.POST['name']
        message=request.POST['message']
        email=request.POST['email']
        city=request.POST['city']

        rev=review.objects.create(name=name,message=message,email=email,city=city)
        rev.save()
      
        return redirect('seemore')

    context = {}
    return render(request, 'app/review.html', context)

def smore(request):

    rev=review.objects.all()
    print(rev)
    context = {
        'rw':rev
        }

    return render(request,"app/seemore.html",context)


def update(request,id):
    update_element=User.objects.get(id=id)
    form=userUpdate(request.POST or None,instance=update_element)
  
    if form.is_valid():
        form.save()
        messages.info(request,"----Updated your Profile..!----")
        return redirect("profile")
        return redirect("profile")
    else:
        print('not')

    return render(request,'app/update.html',{'form':form,'id':id})

def about(request):

    return render(request,"app/about.html")

def Client(request):

    if request.method == 'POST':

        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']

        clnt=client.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone)
        clnt.save()
      
        return redirect('home')

    context = {}
    return render(request, 'app/client.html', context)
       