from django.contrib.auth.models import User
from django.db import models

from product.models import Product
from review.models import Review
from specification.models import Specification
from tag.models import Tag


class Order(models.Model):
    DELIVERY_CHOICES = (
        ("express", "express"),
        ("ordinary", "ordinary"),
    )

    PAYMENT_CHOICES = (
        ("online", "online"),
        ("someone", "someone"),
    )

    STATUS_CHOICES = (
        ("accepted", "accepted"),
        ("processing", "processing"),
    )
    createdAt = models.DateTimeField(auto_now=True)
    fullName = models.CharField(
        blank=True, null=True, max_length=128, verbose_name="Полное имя"
    )
    email = models.EmailField(blank=True, null=True, max_length=128)
    phone = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Номер телефона"
    )
    deliveryType = models.CharField(
        default="ordinary", max_length=8, choices=DELIVERY_CHOICES
    )
    paymentType = models.CharField(
        default="online", max_length=7, choices=PAYMENT_CHOICES
    )
    totalCost = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2
    )
    status = models.CharField(
        default="processing", max_length=10, choices=STATUS_CHOICES
    )
    city = models.CharField(
        blank=True, null=True, max_length=128, verbose_name="Название города"
    )
    address = models.CharField(
        blank=True, null=True, max_length=256, verbose_name="Название города"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")

    def __str__(self) -> str:
        return f"Order (pk={self.pk}, user={self.user})"


class OrderedProduct(models.Model):
    """Модель заказаных продуктов"""

    category = models.IntegerField(default=1)
    price = models.FloatField(default=1.01)
    count = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    fullDescription = models.TextField(blank=True, null=True)
    freeDelivery = models.BooleanField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name="ordredproduct_tag", blank=True)
    reviews = models.ManyToManyField(
        Review, related_name="ordredproduct_review", blank=True
    )

    rating = models.FloatField(blank=True, null=True)
    salePrice = models.FloatField(blank=True, null=True)
    dateFrom = models.DateTimeField(editable=True, blank=True, null=True)
    dateTo = models.DateTimeField(editable=True, blank=True, null=True)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="orderedproduct_order",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"OrderedProduct (pk={self.pk}, title={self.title})"


class OrderImage(models.Model):
    """Модель для хранения картинки заказаных продуктов"""

    src = models.ImageField(
        upload_to="app_users/orderedproducts/",
        default="app_users/orderedproducts/default.png",
        verbose_name="Ссылка",
    )
    alt = models.CharField(
        max_length=128, default="Just an image", verbose_name="Описание"
    )
    ordredproduct = models.ForeignKey(
        OrderedProduct,
        on_delete=models.CASCADE,
        related_name="ordredproduct_images",
        verbose_name="Linked to product:",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "OrderImage"
        verbose_name_plural = "OrderImages"

    def __str__(self) -> str:
        return f"Image: {self.src.name}"
