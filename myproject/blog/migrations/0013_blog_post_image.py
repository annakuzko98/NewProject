# Generated by Django 4.2.3 on 2023-07-30 12:19

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blog_post_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]
