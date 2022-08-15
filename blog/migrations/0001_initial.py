# Generated by Django 4.1 on 2022-08-15 02:22

import datetime
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
                ("titulo", models.CharField(max_length=200)),
                ("cuerpo", models.TextField()),
                ("fecha", models.DateTimeField(verbose_name=datetime.date.today)),
                ("imagen", models.ImageField(blank=True, upload_to="blog/imagenes/")),
            ],
        ),
    ]