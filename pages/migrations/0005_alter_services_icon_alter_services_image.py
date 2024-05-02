# Generated by Django 4.2.7 on 2024-05-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_contactus_alter_services_icon_alter_services_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="icon",
            field=models.ImageField(upload_to="services/"),
        ),
        migrations.AlterField(
            model_name="services",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="services/"),
        ),
    ]
