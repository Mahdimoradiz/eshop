# Generated by Django 5.0.2 on 2024-03-02 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='username',
        ),
    ]