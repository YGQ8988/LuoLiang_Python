from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'qianxiang.html')

def about(request):
    return render(request,'index.asp')

def product(request):
    return render(request,'product.asp')

def anli(request):
    return render(request,'anli.asp')

def acontact(request):
    return render(request,'contact.asp')