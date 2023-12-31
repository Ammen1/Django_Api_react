# Generated by Django 4.2.2 on 2023-06-18 20:14

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                (
                    "audio",
                    models.FileField(
                        default="posts/default.mp3",
                        upload_to=base.models.upload_to,
                        verbose_name="Audio",
                    ),
                ),
                ("excerpt", models.TextField(null=True)),
                ("content", models.TextField()),
                ("word_count", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ("word_count",),
            },
        ),
    ]
