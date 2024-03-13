# Generated by Django 5.0.3 on 2024-03-12 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('product', '0005_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='more_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='contenttypes.contenttype'),
        ),
    ]