# Generated by Django 5.0.2 on 2024-02-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tage_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/image'),
            preserve_default=False,
        ),
    ]
