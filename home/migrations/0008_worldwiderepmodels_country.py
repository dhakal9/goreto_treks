# Generated by Django 5.0 on 2024-08-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_worldwiderepmodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldwiderepmodels',
            name='country',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
