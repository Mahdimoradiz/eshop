# Generated by Django 5.0.3 on 2024-03-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='suggeste',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]