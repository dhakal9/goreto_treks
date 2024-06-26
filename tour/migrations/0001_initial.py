# Generated by Django 5.0 on 2024-05-11 18:52

import django.db.models.deletion
import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationModel',
            fields=[
                ('destination_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=255)),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('slug', models.SlugField(default='default')),
            ],
        ),
        migrations.CreateModel(
            name='FaqModels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=250)),
                ('answer', django_summernote.fields.SummernoteTextField()),
                ('is_global', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='IncludeExcludeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('is_include', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_nav', models.BooleanField(default=False)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destinationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetailsModel',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('depature', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.TimeField(null=True)),
                ('start_end', models.CharField(blank=True, max_length=200, null=True)),
                ('max_price', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(max_length=200)),
                ('transport', models.CharField(blank=True, max_length=200, null=True)),
                ('season', models.CharField(blank=True, max_length=200, null=True)),
                ('altitude', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('days', models.CharField(blank=True, max_length=200, null=True)),
                ('map', models.URLField(blank=True, db_index=True, unique=True)),
                ('map_overview', django_summernote.fields.SummernoteTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('is_activity', models.BooleanField(default=False)),
                ('is_attraction', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destinationmodel')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.regionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ItinatyModel',
            fields=[
                ('itinary_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=2)),
                ('start_end', models.CharField(blank=True, max_length=200, null=True)),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourdetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='GallaryModel',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourdetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TourFaqModels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.faqmodels')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourdetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TourIncludeExcludeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_included', models.BooleanField(default=True)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.includeexcludemodel')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourdetailsmodel')),
            ],
            options={
                'unique_together': {('tour', 'sentence')},
            },
        ),
    ]
