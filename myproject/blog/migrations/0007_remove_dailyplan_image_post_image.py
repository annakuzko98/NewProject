# Generated by Django 4.2.3 on 2023-07-28 10:57

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_dailyplan_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyplan',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]
