# Generated by Django 2.0.4 on 2018-05-02 23:04

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='color',
            field=colorful.fields.RGBColorField(),
        ),
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_20185223443cb7c73ec', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_20185223443346d2670', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
