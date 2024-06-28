# Generated by Django 4.2.7 on 2024-06-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_delete_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="OurTeam",
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
                ("name", models.CharField(max_length=255)),
                ("roll", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="Team/")),
                ("social_media_link", models.URLField(max_length=255)),
            ],
        ),
    ]
