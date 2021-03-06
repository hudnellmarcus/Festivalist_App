# Generated by Django 4.0.6 on 2022-07-14 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festivalist_app', '0020_festival_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='festivalist_app.photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
