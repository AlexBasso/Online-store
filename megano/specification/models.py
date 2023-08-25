from django.db import models


class Specification(models.Model):
    """Модель продуктов"""

    name = models.CharField(max_length=128)
    value = models.TextField()

    def __str__(self) -> str:
        return f"Specification: {self.name}"
