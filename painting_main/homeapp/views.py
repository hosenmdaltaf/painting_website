from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Services,Review,Contact,Gallery, Slider
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    services= Services.objects.all()
    reviews= Review.objects.all()
    sliders= Slider.objects.all()
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)

            subject = 'Message from holidayzbd.Contact  page'
            message = f'This is user-----> Name:{name}, E-mail:{email},Message{message},Phonenumber{phone}.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['altafhm2000@gmail.com']) 

            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    context ={
        'services':services,
        'reviews':reviews,
        'sliders':sliders
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

            subject = 'Message from holidayzbd.Contact  page'
            message = f'This is user-----> Name:{name}, E-mail:{email},Message{message},Phonenumber{phone}.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['altafhm2000@gmail.com']) 

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

            subject = 'Message from holidayzbd.Contact  page'
            message = f'This is user-----> Name:{name}, E-mail:{email},Message{message},Phonenumber{phone}.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['altafhm2000@gmail.com']) 

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

            subject = 'Message from holidayzbd.Contact  page'
            message = f'This is user-----> Name:{name}, E-mail:{email},Message{message},Phonenumber{phone}.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['altafhm2000@gmail.com']) 

            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')

    return render(request,'homeapp/contact.html')


def services_details(request,pk):
    data = Services.objects.get(pk=pk)
    services= Services.objects.all()
    if request.method =="POST":
        try:
            name= request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            services= request.POST.get('services')
            message= request.POST.get('message')
            Contact.objects.create(name=name,email=email,phone=phone,services=services,message=message)


            subject = 'Message from holidayzbd.Contact  page'
            message = f'This is user-----> Name:{name}, E-mail:{email},Message{message},Phonenumber{phone}.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['altafhm2000@gmail.com']) 

            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')

    context={
        'data':data,
        'services':services
    }
    return render(request,'homeapp/service_details.html',context)



