# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UUID', models.IntegerField()),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField(verbose_name='Date of birth: ')),
                ('Sex', models.CharField(max_length=1, verbose_name='F/M: ')),
                ('Batch', models.IntegerField(verbose_name='Batch: ')),
                ('sap_id', models.IntegerField(verbose_name='SAP ID: ')),
                ('Div', models.CharField(max_length=5, verbose_name='Division: ')),
                ('Year', models.IntegerField(verbose_name='Year: ')),
                ('Course', models.CharField(max_length=20, verbose_name='Course: ')),
                ('Stream', models.CharField(max_length=10, verbose_name='Stream: ')),
                ('Email', models.CharField(max_length=50, verbose_name='email: ')),
                ('Phone', models.IntegerField(verbose_name='phone number: ')),
                ('Address', models.CharField(max_length=200, verbose_name='Address: ')),
            ],
        ),
    ]
