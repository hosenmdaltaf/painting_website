
from django.db import models

# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.
class Services(models.Model):
    name= models.CharField(max_length=255, null=True)
    short_description =models.TextField(null=True,blank=True)
    details = models.TextField(null=True,blank=True)
    thumnail_images =  models.ImageField(null=True,blank=True)

    def __str__(self):
        return str(self.name) 

    def image_tag(self):
        if self.thumnail_images != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_images))


class Gallery(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 

    def image_tag(self):
        if self.thumnail_images != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_images))


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 

class Review(models.Model):
    name = models.CharField(max_length=255, null=True)
    details = models.TextField(max_length=255, null=True)

    def __str__(self):
        return str(self.name) 