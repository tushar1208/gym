from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def classes(request):
    return render(request,'classes.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def account(request):
    return render(request,'account.html')

def login(request):
    return render(request,'login.html')

# def photo(request):
#     return render(request,'photo.html')

