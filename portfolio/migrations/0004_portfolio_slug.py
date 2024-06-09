# Generated by Django 4.2.7 on 2024-06-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_alter_portfolio_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="slug",
            field=models.SlugField(default=2, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]