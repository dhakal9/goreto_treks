# Generated by Django 5.0 on 2024-06-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_alter_tourdetailsmodel_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetailsmodel',
            name='itinary_pdf',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
