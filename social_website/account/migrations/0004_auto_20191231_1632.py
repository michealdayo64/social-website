# Generated by Django 2.2.6 on 2020-01-01 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191231_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_of_birth',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
