# Generated by Django 2.1 on 2019-11-24 01:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 24, 1, 37, 25, 177080, tzinfo=utc)),
        ),
    ]
