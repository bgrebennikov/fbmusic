# Generated by Django 2.1.4 on 2019-01-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190108_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbtracks',
            name='title',
        ),
        migrations.AddField(
            model_name='dbtracks',
            name='artist',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='dbtracks',
            name='trackName',
            field=models.CharField(default='', max_length=120),
        ),
    ]
