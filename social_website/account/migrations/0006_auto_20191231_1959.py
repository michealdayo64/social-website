# Generated by Django 2.2.6 on 2020-01-01 03:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191231_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 1, 3, 59, 20, 526633, tzinfo=utc)),
        ),
    ]