# Generated by Django 4.1.6 on 2023-03-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_car_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]