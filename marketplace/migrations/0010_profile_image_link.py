# Generated by Django 2.0.2 on 2018-05-21 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_auto_20180521_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
