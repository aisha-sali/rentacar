# Generated by Django 4.1.3 on 2022-12-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
