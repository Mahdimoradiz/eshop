# Generated by Django 5.0.3 on 2024-03-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_discountcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
