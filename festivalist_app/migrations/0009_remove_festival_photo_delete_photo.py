# Generated by Django 4.0.6 on 2022-07-13 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivalist_app', '0008_remove_festival_photo_festival_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festival',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]