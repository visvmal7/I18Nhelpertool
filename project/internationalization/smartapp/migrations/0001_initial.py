# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NBUList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('appname', models.CharField(max_length=255)),
                ('version_num', models.CharField(max_length=255)),
                ('storage_name', models.CharField(max_length=255)),
                ('protocol_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NbuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browse', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.CharField(choices=[('NetApp 7-Mode', 'NetApp 7-Mode'), ('NetApp C-Mode', 'NetApp C-Mode'), ('EMC-VNX', 'EMC-VNX')], max_length=20)),
                ('version', models.CharField(choices=[('7.5.0.7', '7.5.0.7'), ('7.6.0.4', '7.6.0.4'), ('7.6.1.2', '7.6.1.2'), ('7.7.1', '7.7.1'), ('7.7.2', '7.7.2')], max_length=10)),
                ('snapshot', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('replication', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('liveBrowse', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('index', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('PIT_Rollback', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('SFR', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
                ('dataMover', models.CharField(choices=[('Supported', 'Supported'), ('Not Supported', 'Not Supported'), ('Not Applicable', 'Not Applicable')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RDProtocol',
            fields=[
                ('protocol_standard', models.CharField(choices=[('NAS', 'NAS'), ('SAN', 'SAN')], max_length=10)),
                ('protocolname', models.CharField(choices=[('NFS', 'NFS'), ('CIFS', 'CIFS'), ('NDMP', 'NDMP'), ('ISCSI', 'iSCSI'), ('FC', 'FC')], max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TokenNumberNew',
            fields=[
                ('tok_number', models.PositiveIntegerField(blank=True, default=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('description', models.CharField(max_length=100)),
                ('code', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('description', models.CharField(max_length=100)),
                ('code', models.SlugField(primary_key=True, serialize=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartapp.VehicleBrand')),
            ],
        ),
        migrations.AddField(
            model_name='rd',
            name='rdprotocol',
            field=models.ForeignKey(default='NAS', on_delete=django.db.models.deletion.CASCADE, to='smartapp.RDProtocol'),
        ),
    ]
