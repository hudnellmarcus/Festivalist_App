# Generated by Django 4.0.6 on 2022-07-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalist_app', '0014_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
