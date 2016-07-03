# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nazwa galerii')),
                ('slug', models.SlugField(null=True, verbose_name=b'Odnosnik', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data dodania')),
                ('cover', models.ImageField(upload_to=b'static/galleries/covers/%Y/%m/%d', verbose_name=b'Ok\xc5\x82adka')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerie',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/galleries/%Y/%m/%d', verbose_name=b'Zdj\xc4\x99cie')),
                ('thumbnail', models.ImageField(null=True, upload_to=b'static/galleries/thumbnails/%Y/%m/%d', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data dodania')),
                ('description', models.CharField(max_length=160, null=True, verbose_name=b'Opis zdj\xc4\x99cia', blank=True)),
                ('gallery', models.ForeignKey(to='bajkamiutkane.Gallery')),
            ],
            options={
                'verbose_name': 'Zdj\u0119cie',
                'verbose_name_plural': 'Zdj\u0119cia',
            },
        ),
    ]
