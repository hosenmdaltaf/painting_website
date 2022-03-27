from django.http import HttpResponse
from django.shortcuts import render
from .models import Services


# Create your views here.
def home(request):
    return render(request,'homeapp/home.html')

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
    return HttpResponse(data.name,data.thumnail_images)
