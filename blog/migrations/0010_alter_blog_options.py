# Generated by Django 5.0.2 on 2024-02-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_options_remove_blog_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_at']},
        ),
    ]
