# Generated by Django 2.2.6 on 2020-01-02 00:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200101_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 2, 0, 25, 42, 988843, tzinfo=utc)),
        ),
    ]
