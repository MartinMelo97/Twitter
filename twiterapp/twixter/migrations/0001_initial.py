# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Twixt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_user', models.CharField(max_length=50)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique_for_date='creado')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-fecha',),
            },
        ),
    ]
