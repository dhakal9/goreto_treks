# Generated by Django 5.0 on 2024-07-22 09:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0012_alter_destinationmodel_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialModels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trekking_des', ckeditor.fields.RichTextField()),
                ('goreto_special_des', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
