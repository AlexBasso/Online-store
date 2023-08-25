from django.db import models


class Tag(models.Model):
    """Модель Тэгов продукта"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
