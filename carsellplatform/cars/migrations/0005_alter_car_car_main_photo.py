# Generated by Django 4.1.6 on 2023-03-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carphoto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_main_photo',
            field=models.ImageField(blank=True, default='photos/cars/ghost.png', null=True, upload_to='photos/cars/%Y/%m/%d/'),
        ),
    ]
