# Generated by Django 5.0.4 on 2024-06-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="number_version",
            field=models.IntegerField(verbose_name="Номер версии"),
        ),
    ]
