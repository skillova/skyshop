# Generated by Django 5.0.4 on 2024-06-22 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_version_number_version"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name"],
                "permissions": [
                    ("can_set_product", "can set product"),
                    ("can_edit_description", "can edit description"),
                    ("can_edit_category", "can edit category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
