# Generated by Django 3.2.12 on 2022-09-04 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historymodels',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 5, 21, 47, 210821)),
        ),
    ]