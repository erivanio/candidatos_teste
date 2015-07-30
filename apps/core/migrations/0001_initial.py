# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name': 'Cadidato',
                'verbose_name_plural': 'Candidatos',
            },
            bases=(models.Model,),
        ),
    ]
