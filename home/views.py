from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is homepage.')

def addproduct(request):
    return HttpResponse('This is the page to add products.')

def login(request):
    return HttpResponse('This is the login page.')

def signup(request):
    return HttpResponse('This is the signup page.')