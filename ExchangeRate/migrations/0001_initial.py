# Generated by Django 3.0.6 on 2020-05-21 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetScrapy',
            fields=[
                ('bank', models.CharField(max_length=25)),
                ('currency_name', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('buying_rate', models.CharField(max_length=20)),
                ('selling_rate', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Exchange_Rates',
                'ordering': ['currency_name', 'bank'],
            },
        ),
    ]
