from django.contrib import admin
from .models import Contact,Services,Gallery,Review

# Register your models here.

class Contactlist(admin.ModelAdmin):
    list_display = ('name','phone','email','message')
admin.site.register(Contact,Contactlist)

class Serviceslist(admin.ModelAdmin):
    list_display = ('name','image_tag')
admin.site.register(Services,Serviceslist)

class Gallerylist(admin.ModelAdmin):
    list_display = ('name','image_tag')
admin.site.register(Gallery,Gallerylist)

admin.site.register(Review)