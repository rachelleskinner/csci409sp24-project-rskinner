# Generated by Django 5.0.2 on 2024-03-05 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vesselschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillOfLading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bol_number', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('release_status', models.CharField(choices=[('C', 'Customs Hold'), ('S', 'Steamship Hold'), ('R', 'Released'), ('A', 'Available for Pickup')], max_length=1)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.vessel')),
            ],
        ),
    ]
