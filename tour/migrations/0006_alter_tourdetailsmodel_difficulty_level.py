# Generated by Django 5.0 on 2024-05-31 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_alter_tourdetailsmodel_difficulty_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourdetailsmodel',
            name='difficulty_level',
            field=models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('difficult', 'Difficult')], default='moderate', max_length=10),
        ),
    ]
