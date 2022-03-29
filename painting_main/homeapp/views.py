from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Services,Review,Contact,Gallery
from django.contrib import messages


# Create your views here.
def home(request):
    services= Services.objects.all()
    reviews= Review.objects.all()
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    context ={
        'services':services,
        'reviews':reviews
    }
    return render(request,'homeapp/home.html',context)

def about(request):
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'homeapp/about.html')

def works(request):
    galleries = Gallery.objects.all()
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'homeapp/works.html',{'galleries':galleries})

def services(request):
    services= Services.objects.all()
    return render(request,'homeapp/service.html',{'services':services})

def contact(request):
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')

    return render(request,'homeapp/contact.html')


# def contact(request):
#     if request.method == "POST":
#         try:
#             name = request.POST.get("name")
#             email = request.POST.get("email")
#             message = request.POST.get("message")
#             phonenumber = request.POST.get("phonenumber") 
#             print('----------------------test1------------------')
#             print(name)
#             print(email)
#             print(message)
#             print(phonenumber)
#             Contact.objects.create(name=name,message=message,phonenumber=phonenumber,email=email)
#             return render(request,'global/thankyou.html')
#         except:
#             messages.warning(request, 'Please fill up all the form feild currectly!')
#     return render(request,'contactapp/contact.html')

def services_details(request,pk):
    data = Services.objects.get(pk=pk)
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    context={
        'data':data
    }
    return render(request,'homeapp/service_details.html',context)
