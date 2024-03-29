
from statistics import mode
from django.db import models

# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.
class Services(models.Model):
    name= models.CharField(max_length=255, null=True)
    short_description =models.TextField(null=True,blank=True)
    details = models.TextField(null=True,blank=True)
    thumnail_images =  models.ImageField(null=True,blank=True,upload_to="services_images")

    def __str__(self):
        return str(self.name) 

    def image_tag(self):
        if self.thumnail_images != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_images))


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images",null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255, null=True)
    services = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 

class Review(models.Model):
    name = models.CharField(max_length=255, null=True)
    details = models.TextField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 

class Slider(models.Model):
    text= models.CharField(max_length=255, null=True)
    slider_image= models.ImageField(upload_to="slider_images")