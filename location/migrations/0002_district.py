# Generated by Django 3.1.6 on 2021-02-20 17:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_id', models.IntegerField()),
                ('district', models.CharField(max_length=18)),
                ('zone_name', models.CharField(max_length=16)),
                ('region', models.CharField(max_length=16)),
                ('diss', models.IntegerField()),
                ('xc', models.FloatField()),
                ('yc', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
