# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModulesInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('opleiding', models.CharField(default='Opleiding', max_length=35)),
                ('gebied', models.CharField(choices=[('studie', 'studie'), ('sociaal', 'sociaal'), ('toekomst', 'toekomst'), ('studiesociaal', 'studiesociaal'), ('studietoekomst', 'studietoekomst'), ('sociaaltoekomst', 'sociaaltoekomst')], default='studie', max_length=50)),
                ('naam', models.CharField(default='NAAM', max_length=50)),
                ('id_module', models.CharField(default='', max_length=15)),
                ('omschrijving', models.TextField(default='OMSCHRIJVING')),
                ('tijd', models.IntegerField(verbose_name='Tijdsduur', default=0)),
                ('kosten', models.IntegerField(verbose_name='Kosten', default=0)),
                ('baten_vast', models.IntegerField(verbose_name='Vaste baten', default=0)),
                ('baten_flex', models.IntegerField(verbose_name='Flexibele baten', default=0)),
                ('experience_vast', models.IntegerField(verbose_name='Vaste exp', default=0)),
                ('experience_flex', models.IntegerField(verbose_name='Flexibele exp', default=0)),
                ('factor', models.PositiveIntegerField(verbose_name='Factor module', default=0)),
                ('niveau', models.IntegerField(verbose_name='Niveau van course', default=1)),
                ('module_type', models.CharField(default='Passief', max_length=15)),
                ('exp_required', models.IntegerField(verbose_name='Experience benodigd', default=0)),
                ('date1', models.DateTimeField(default=datetime.datetime(2016, 7, 1, 0, 0))),
                ('date2', models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0))),
                ('date3', models.DateTimeField(default=datetime.datetime(2016, 4, 1, 0, 0))),
            ],
        ),
    ]
