# Generated by Django 4.1.8 on 2023-05-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_store", "0003_remove_user_is_superuser_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reset_token",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
