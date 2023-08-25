from django.db import models

from product.models import Product


class Image(models.Model):
    """Модель для хранения картинки продукта"""

    src = models.ImageField(
        upload_to="app_users/CatalogItem/",
        default="app_users/CatalogItem/default.png",
        verbose_name="Ссылка",
    )
    alt = models.CharField(
        max_length=128, default="Just an image", verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        return f"Image: {self.src.name}"


class CatalogItems(models.Model):
    title = models.CharField(max_length=128)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="catalogitems_image",
        verbose_name="Image",
        blank=True,
        null=True,
    )
    subcategories = models.ManyToManyField(
        "self",
        blank=True,
    )

    class Meta:
        verbose_name = "CatalogItems"
        verbose_name_plural = "CatalogItems's"

    def __str__(self) -> str:
        return f"CatalogItems (pk={self.pk}, title={self.title})"


class CatalogItem(models.Model):
    currentPage = models.IntegerField(default=1)
    lastPage = models.IntegerField(default=1)
    items = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = "CatalogItem"
        verbose_name_plural = "CatalogItem's"

    def __str__(self) -> str:
        return f"CatalogItem (pk={self.pk})"


class SalesItem(models.Model):
    currentPage = models.IntegerField(default=1)
    lastPage = models.IntegerField(default=1)
    items = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = "SalesItem"
        verbose_name_plural = "SalesItem's"

    def __str__(self) -> str:
        return f"SalesItem (pk={self.pk})"
