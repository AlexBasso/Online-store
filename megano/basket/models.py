from django.db import models
from django.contrib.auth.models import User

from auth_user.models import Profile
from product.models import Product


class OrderProduct(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orderproduct_product",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"OrderProduct (pk={self.pk}, title={self.product.title})"


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="basket")
    products = models.ManyToManyField(
        OrderProduct, related_name="basket_orderproduct", blank=True
    )

    def __str__(self) -> str:
        return f"Basket (pk={self.pk}, title={self.user})"
