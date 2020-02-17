# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 05:29
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


INVITE_TO_STREAM_POLICY_MEMBERS = 1
def handle_waiting_period(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    Realm = apps.get_model('zerver', 'Realm')
    Realm.INVITE_TO_STREAM_POLICY_WAITING_PERIOD = 3
    Realm.objects.filter(waiting_period_threshold__gt=0).update(
        invite_to_stream_policy=Realm.INVITE_TO_STREAM_POLICY_WAITING_PERIOD)

class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0213_realm_digest_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='invite_to_stream_policy',
            field=models.PositiveSmallIntegerField(default=INVITE_TO_STREAM_POLICY_MEMBERS),
        ),
        migrations.RunPython(handle_waiting_period,
                             reverse_code=migrations.RunPython.noop),
    ]
