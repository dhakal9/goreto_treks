# Generated by Django 5.0 on 2024-04-10 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_companyprofile_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteammodel',
            name='message',
            field=models.TextField(default='hello nepal'),
        ),
    ]
