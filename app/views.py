from django.shortcuts import render,HttpResponse

# Create your views here.

def home(req):
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def shop(req):
    return render(req,'shop.html')

def blog(req):
    return render(req,'blog.html')