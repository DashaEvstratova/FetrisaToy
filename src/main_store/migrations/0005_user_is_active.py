# Generated by Django 4.1.8 on 2023-04-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_store", "0004_alter_pictures_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]