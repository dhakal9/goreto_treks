# Generated by Django 5.0 on 2024-02-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_rename_destinati_id_destinationmodel_destination_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourdetailsmodel',
            old_name='actvity_id',
            new_name='activity_id',
        ),
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
