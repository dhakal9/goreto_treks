# Generated by Django 5.0 on 2024-08-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0016_alter_itinatymodel_day_alter_itinatymodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetailsmodel',
            name='price_1',
            field=models.CharField(blank=True, default='20$', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tourdetailsmodel',
            name='price_2',
            field=models.CharField(blank=True, default='20$', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tourdetailsmodel',
            name='price_35',
            field=models.CharField(blank=True, default='20$', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tourdetailsmodel',
            name='price_510',
            field=models.CharField(blank=True, default='20$', max_length=200, null=True),
        ),
    ]
