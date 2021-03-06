# Generated by Django 3.1.4 on 2021-01-11 03:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_organization', models.CharField(max_length=100, verbose_name='管理者')),
            ],
            options={
                'verbose_name_plural': '管理者',
                'db_table': 'management_organization',
            },
        ),
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bridge_id', models.IntegerField(verbose_name='橋梁ID')),
                ('bridge_name', models.CharField(max_length=100, verbose_name='橋梁名称')),
                ('bridge_name_yomi', models.CharField(blank=True, max_length=100, verbose_name='橋梁名称カタカナ')),
                ('location_city', models.CharField(max_length=100, verbose_name='所在地 市町村')),
                ('location_address', models.CharField(blank=True, max_length=255, verbose_name='所在地')),
                ('road_cd', models.IntegerField(verbose_name='路線番号')),
                ('road_name', models.CharField(max_length=100, verbose_name='路線名')),
                ('fyear_start', models.IntegerField(blank=True, null=True, verbose_name='供用年')),
                ('len_m', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='橋長m')),
                ('wid_m', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='幅員m')),
                ('span_num', models.IntegerField(blank=True, null=True, verbose_name='径間数')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='緯度')),
                ('longtitude', models.FloatField(blank=True, null=True, verbose_name='経度')),
                ('have_alternative', models.BooleanField(blank=True, default=False, null=True, verbose_name='代替路')),
                ('date_register', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='入力年月日')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('management_organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bridges.managementorganization')),
            ],
            options={
                'verbose_name_plural': '橋梁',
                'db_table': 'bridge',
                'unique_together': {('bridge_id', 'management_organization')},
            },
        ),
    ]
