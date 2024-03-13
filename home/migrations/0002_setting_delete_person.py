# Generated by Django 5.0.3 on 2024-03-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='site/settings')),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]