from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    return HttpResponse('This is homepage.')

def addproduct(request):
    return HttpResponse('This is the page to add products.')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()
            login(request,user)
            return render(request,'home.html')

    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'form':form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            #log the user in
            return render(request,'login.html')

    else:
        form = UserCreationForm

    return render(request,'signup.html',{'form':form})
    
    
    

def contactus(request):
    return HttpResponse('This is the Contact Us page.')