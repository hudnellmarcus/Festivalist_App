# Generated by Django 4.0.6 on 2022-07-14 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivalist_app', '0017_remove_photo_url'),
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
