# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150730_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='andoird',
        ),
        migrations.AddField(
            model_name='candidate',
            name='android',
            field=models.IntegerField(null=True, verbose_name=b'Desenvolvimento Android', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='ios',
            field=models.IntegerField(null=True, verbose_name=b'Desenvolvimento IOS', blank=True),
            preserve_default=True,
        ),
    ]
