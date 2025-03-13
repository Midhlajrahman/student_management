# Generated by Django 5.1.5 on 2025-03-12 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_rename_pdf_note_file"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Commend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "is_active",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=True,
                        verbose_name="Mark as Active",
                    ),
                ),
                ("commend", models.TextField()),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(app_label)s_%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.subject"
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]
