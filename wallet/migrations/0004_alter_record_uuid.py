# Generated by Django 4.2.3 on 2023-07-04 12:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0003_alter_iamuser_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
