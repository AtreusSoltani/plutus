# Generated by Django 4.2.3 on 2023-07-04 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0002_remove_iamuser_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="iamuser",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
