# Generated by Django 5.0 on 2024-02-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_rename_actvity_id_tourdetailsmodel_activity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationmodel',
            name='name',
            field=models.ImageField(upload_to=None),
        ),
        migrations.AlterField(
            model_name='itinatymodel',
            name='day',
            field=models.IntegerField(),
        ),
    ]
