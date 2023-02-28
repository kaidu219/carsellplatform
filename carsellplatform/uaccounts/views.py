from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from cars.models import Car


def login(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        # username = username.lower()
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            return redirect('login')
    
    return render(request, 'uaccounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This user already exists!')
                return redirect('login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists!')
                    return redirect('login')
                else:
                    user = User.objects.create_user(first_name=first_name, 
                                                    last_name=last_name, email=email, 
                                                    username=username, password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in!')
                    return redirect('dashboard')
        else:
            return redirect('register')
             
    else:
        return render(request, 'uaccounts/register.html') 


@login_required
def dashboard(request):
    user_id = request.user.id
    allInquires = Contact.objects.all().order_by('-created_date').filter(user_id=user_id)
    carList = [i.car_id for i in allInquires]
    carListView = []
    
    for cl in carList:
        car = Car.objects.get(id = cl)
        carListView.append(car)
        
    context = {
        'allInquires': allInquires,
        'cars': carListView,
    }
    
    return render(request, 'uaccounts/dashboard.html', context)