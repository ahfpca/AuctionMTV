# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auto_20180529_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='media',
            name='genre',
        ),
        migrations.AddField(
            model_name='media',
            name='fk_genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_media', to='auction.Genre'),
            preserve_default=False,
        ),
    ]
