# Generated by Django 4.2.4 on 2023-08-21 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_number',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
