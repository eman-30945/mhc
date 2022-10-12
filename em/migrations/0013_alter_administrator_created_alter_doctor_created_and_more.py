# Generated by Django 4.1.1 on 2022-10-10 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0012_alter_administrator_created_alter_doctor_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 20, 48, 50, 933905)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 20, 48, 50, 933905)),
        ),
        migrations.AlterField(
            model_name='employee_form',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 20, 48, 50, 933905)),
        ),
        migrations.AlterField(
            model_name='nursing',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 20, 48, 50, 933905)),
        ),
    ]
