# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdb', '0002_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='codigo_e',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
