# Generated by Django 5.0 on 2024-07-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_ourteammodel_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seomodel',
            name='discription',
            field=models.TextField(),
        ),
    ]