# Generated by Django 4.2.3 on 2023-07-13 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 13, 12, 34, 34, 105784)
            ),
        ),
    ]