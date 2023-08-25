from django.db import models


class Review(models.Model):
    """Модель отзывов"""

    author = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField(max_length=512, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Review author:{self.author}, text:{self.text[:16]}...)"
