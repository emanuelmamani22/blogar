# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdb', '0004_auto_20160112_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido_c', models.TextField()),
                ('numero_c', models.IntegerField()),
                ('codigo_p', models.ForeignKey(to='blogdb.Post')),
            ],
        ),
    ]
