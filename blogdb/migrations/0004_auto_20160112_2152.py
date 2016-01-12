# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdb', '0003_post_codigo_e'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='codigo_e',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
