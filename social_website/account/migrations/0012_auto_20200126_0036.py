# Generated by Django 2.2.6 on 2020-01-26 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200121_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 26, 8, 36, 13, 446851, tzinfo=utc)),
        ),
    ]
