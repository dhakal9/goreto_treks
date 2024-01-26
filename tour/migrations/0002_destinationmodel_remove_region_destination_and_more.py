# Generated by Django 5.0 on 2024-01-26 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationModel',
            fields=[
                ('destinati_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.ImageField(upload_to=None)),
                ('slogan', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=10000)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='region',
            name='destination',
        ),
        migrations.RenameModel(
            old_name='Activities',
            new_name='ActivitiesModel',
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('region_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('discription', models.TextField(max_length=2000)),
                ('is_active', models.BooleanField(default=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destinationmodel')),
            ],
        ),
        migrations.AlterField(
            model_name='activitiesmodel',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.regionmodel'),
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
