# Generated by Django 5.0 on 2024-01-28 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_rename_discription_regionmodel_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourDetailsModel',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('depature', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('start_end', models.CharField(blank=True, max_length=200, null=True)),
                ('max_price', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(max_length=200)),
                ('transport', models.CharField(blank=True, max_length=200, null=True)),
                ('season', models.CharField(blank=True, max_length=200, null=True)),
                ('altitude', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('days', models.CharField(blank=True, max_length=200, null=True)),
                ('map', models.URLField(blank=True, db_index=True, max_length=2048, unique=True)),
                ('map_overview', models.TextField(max_length=2000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('is_activity', models.BooleanField(default=False)),
                ('is_acttraction', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destinationmodel')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.regionmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='ActivitiesModel',
        ),
    ]
