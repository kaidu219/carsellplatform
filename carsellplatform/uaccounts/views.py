from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from cars.models import Car
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm

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

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'uaccounts/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        context['allInquires'] = Contact.objects.all().order_by('-created_date').filter(user_id=user_id)
        carList = [i.car_id for i in context['allInquires']]
        carListView = []
    
        for cl in carList:
            car = Car.objects.get(id = cl)
            carListView.append(car)
        context['cars'] =  carListView  

        return context

# @login_required(login_url='login')
# def dashboard(request):
#     user_id = request.user.id
#     allInquires = Contact.objects.all().order_by('-created_date').filter(user_id=user_id)
#     carList = [i.car_id for i in allInquires]
#     carListView = []
    
#     for cl in carList:
#         car = Car.objects.get(id = cl)
#         carListView.append(car)
        
#     context = {
#         'allInquires': allInquires,
#         'cars': carListView,
#     }
    
#     return render(request, 'uaccounts/dashboard.html', context)


class UsercarsView(LoginRequiredMixin, TemplateView):
    template_name = 'uaccounts/user_cars.html'
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        user = User.objects.get(id = user_id)
        context['usercars'] = user.cars.all()

        return context 
    

# @login_required(login_url='login')
# def user_cars(request):
#     user_id = request.user.id
#     user = User.objects.get(id = user_id)
#     usercars = user.cars.all()
    
#     context = {
#         'user': user,
#         'usercars': usercars,
#     }
#     return render(request, 'uaccounts/user_cars.html', context)


    
class AddCommentView(LoginRequiredMixin, TemplateView):
    def post(self, request, pk, *args, **kwargs):
        car = Car.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.car = car
                comment.user = request.user
                comment.save()
            else:
                messages.warning(request, 'Please log in to add a comment')
                return redirect('login')
        return redirect('cardetails', id=pk)

# @login_required(login_url='login')
# def add_comment(request, pk):
#     car = Car.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
        
#         if form.is_valid():
#             if request.user.is_authenticated:
#                 comment = form.save(commit=False)
#                 comment.car = car
#                 comment.user = request.user
#                 comment.save()
#             else:
#                 messages.warning(request, 'Please log in to add a comment')
#                 return redirect('login')
    
#     return redirect('cardetails', id=pk)