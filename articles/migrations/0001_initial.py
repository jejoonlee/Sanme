# Generated by Django 4.1.3 on 2022-11-19 06:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("maps", "0001_initial"),
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
                ("title", models.CharField(max_length=50)),
                ("day", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("pet", models.BooleanField(default=False)),
                ("content", models.TextField()),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("00:00", "00:00"),
                            ("01:00", "01:00"),
                            ("02:00", "02:00"),
                            ("03:00", "03:00"),
                            ("04:00", "04:00"),
                            ("05:00", "05:00"),
                            ("06:00", "06:00"),
                            ("07:00", "07:00"),
                            ("08:00", "08:00"),
                            ("09:00", "09:00"),
                            ("10:00", "10:00"),
                            ("11:00", "11:00"),
                            ("12:00", "12:00"),
                            ("13:00", "13:00"),
                            ("14:00", "14:00"),
                            ("15:00", "15:00"),
                            ("16:00", "16:00"),
                            ("17:00", "17:00"),
                            ("18:00", "18:00"),
                            ("19:00", "19:00"),
                            ("20:00", "20:00"),
                            ("21:00", "21:00"),
                            ("22:00", "22:00"),
                            ("23:00", "23:00"),
                            ("24:00", "24:00"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "participate_people",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("hit", models.PositiveBigIntegerField(default=0)),
                (
                    "thumbnail",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True, upload_to="images/"
                    ),
                ),
                (
                    "like_user",
                    models.ManyToManyField(
                        related_name="like_post", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "park_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="maps.map"
                    ),
                ),
                (
                    "participate",
                    models.ManyToManyField(
                        related_name="participater", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="articles.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]