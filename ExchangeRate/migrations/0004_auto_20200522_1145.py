# Generated by Django 3.0.6 on 2020-05-22 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExchangeRate', '0003_auto_20200522_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getscrapy',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
