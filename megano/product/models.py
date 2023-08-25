from django.db import models

from review.models import Review
from specification.models import Specification
from tag.models import Tag


class Product(models.Model):
    """Модель продуктов"""

    category = models.IntegerField(default=1)
    models.DecimalField(decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.01)
    count = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    fullDescription = models.TextField(blank=True, null=True)
    freeDelivery = models.BooleanField(blank=True, null=True)
    # images = models.ForeignKey(
    #     Image,
    #     on_delete=models.CASCADE,
    #     related_name="product_image",
    #     verbose_name="Image",
    #     blank=True, null=True,
    # )
    tags = models.ManyToManyField(Tag, related_name="product_tag", blank=True)
    specifications = models.ManyToManyField(
        Specification, related_name="product_specification", blank=True
    )
    reviews = models.ManyToManyField(Review, related_name="product_review", blank=True)

    rating = models.FloatField(blank=True, null=True)

    salePrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=1.01, blank=True, null=True
    )
    dateFrom = models.DateTimeField(editable=True, blank=True, null=True)
    dateTo = models.DateTimeField(editable=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"Product (pk={self.pk}, title={self.title})"


class Image(models.Model):
    """Модель для хранения картинки продукта"""

    src = models.ImageField(
        upload_to="app_users/products/",
        default="app_users/products/default.png",
        verbose_name="Ссылка",
    )
    alt = models.CharField(
        max_length=128, default="Just an image", verbose_name="Описание"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Linked to product:",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        return f"Image: {self.src.name}"
