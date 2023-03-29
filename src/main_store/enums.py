from django.db import models


class Category(models.TextChoices):
    set = "Набор", "Набор"
    Single = "Единичная", "Единичная"
