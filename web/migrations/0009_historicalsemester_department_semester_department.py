# Generated by Django 5.1.5 on 2025-03-12 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0008_historicalcommend_historicaldepartment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsemester",
            name="department",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="web.department",
            ),
        ),
        migrations.AddField(
            model_name="semester",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="web.department",
            ),
            preserve_default=False,
        ),
    ]
