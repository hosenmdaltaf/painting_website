# Generated by Django 3.2 on 2022-03-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_contact_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True)),
                ('slider_image', models.ImageField(upload_to='slider_images')),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery_images'),
        ),
        migrations.AlterField(
            model_name='services',
            name='thumnail_images',
            field=models.ImageField(blank=True, null=True, upload_to='services_images'),
        ),
    ]
