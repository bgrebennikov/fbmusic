# Generated by Django 2.1.4 on 2019-01-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dbtracks_track_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbtracks',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
