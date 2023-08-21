# Generated by Django 4.2.4 on 2023-08-21 10:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('balance', models.BigIntegerField()),
                ('wallet_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wallet.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('type', models.CharField(choices=[('NONE', 'None'), ('TRANSFER', 'Transfer'), ('DEPOSIT', 'Deposit')], default='None', max_length=8)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SUCCESSFUL', 'Successful'), ('REJECTED', 'Rejected')], default='Pending', max_length=10)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('reference_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wallet.wallet')),
            ],
        ),
    ]