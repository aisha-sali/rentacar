# Generated by Django 4.1.3 on 2022-12-11 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_car_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateTimeField(null=True)),
                ('date2', models.DateTimeField(null=True)),
                ('carr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.car')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
