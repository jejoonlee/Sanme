# Generated by Django 4.1.3 on 2022-11-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_delete_park"),
    ]

    operations = [
        migrations.CreateModel(
            name="Search",
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
                ("title", models.CharField(max_length=10)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
