# Generated by Django 5.0.3 on 2024-03-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_more_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
