from django.shortcuts import redirect, render,get_object_or_404
from blogapp.models import Blog,Comment
from homeapp.models import Gallery,Services,Contact
# from servicepage.models import Category,Service

def blog(request):
    blogs = Blog.objects.all()
    latest_blogs = Blog.objects.all().order_by('-post_date')[:3]
    gallerys = Gallery.objects.all()[:6]
    return render(request,'blogapp/blogs.html',{'blogs':blogs,'latest_blogs':latest_blogs,'gallerys':gallerys})

def blog_details(request,pk):
    object = Blog.objects.get(pk=pk)
    latest_blogs = Blog.objects.all().order_by('-post_date')[:3]
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        text = request.POST.get("text")
        print('------------------------------------test result')
        print(text)
        Comment.objects.create(text=text,post=object)
        return redirect("blogapp:blog_details",pk=post.pk )

    if request.method == "POST":
        data = request.POST
        if data['services'] != 'none':
            services = Services.objects.get(id=data['services'])
        else:
            services = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phonenumber") 

        Contact.objects.create(name=name,message=message,phone=phone,services=services)

        # msg = f"""
        # name: {name}.
        # message: {message}. 
        # phonenumber: {phonenumber}.
        # NID Number: {nid}. 
        # Servicesname: {Servicesname}
        # """
        # receiver = '+8801880871297'
        # sms_status = smsapi(receiver, msg)
        return render(request,'global/thankyou.html')


    comments=Comment.objects.filter(post=post)
    return render(request,'blogapp/blog_details.html',{'object':object,'latest_blogs':latest_blogs,
    'comments':comments})
