from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Services,Review


# Create your views here.
def home(request):
    services= Services.objects.all()
    reviews= Review.objects.all()
    context ={
        'services':services,
        'reviews':reviews
    }
    return render(request,'homeapp/home.html',context)

def about(request):
    return render(request,'homeapp/about.html')

def works(request):
    return render(request,'homeapp/works.html')

def services(request):
    return render(request,'homeapp/service.html')

def contact(request):
    return render(request,'homeapp/contact.html')

def services_details(request,pk):
    data = Services.objects.get(pk=pk)
    context={
        'data':data
    }
    return render(request,'homeapp/service_details.html',context)
