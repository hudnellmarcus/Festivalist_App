# Generated by Django 4.0.6 on 2022-07-13 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivalist_app', '0016_alter_photo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
    ]