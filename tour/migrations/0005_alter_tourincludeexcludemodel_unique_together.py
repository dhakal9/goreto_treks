# Generated by Django 5.0 on 2024-04-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_rename_is_acttraction_tourdetailsmodel_is_attraction'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tourincludeexcludemodel',
            unique_together={('tour', 'sentence')},
        ),
    ]
