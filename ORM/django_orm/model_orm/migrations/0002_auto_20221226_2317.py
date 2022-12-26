# Generated by Django 3.2.4 on 2022-12-26 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_orm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 23, 17, 9, 44046)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='number_of_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='number_of_pingbacks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 23, 17, 9, 44046)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]