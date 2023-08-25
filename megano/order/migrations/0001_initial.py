# Generated by Django 4.2 on 2023-08-11 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tag", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now=True)),
                (
                    "fullName",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Полное имя"
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=128, null=True)),
                (
                    "phone",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Номер телефона"
                    ),
                ),
                (
                    "deliveryType",
                    models.CharField(
                        choices=[("express", "express"), ("ordinary", "ordinary")],
                        default="ordinary",
                        max_length=8,
                    ),
                ),
                (
                    "paymentType",
                    models.CharField(
                        choices=[("online", "online"), ("someone", "someone")],
                        default="online",
                        max_length=7,
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("accepted", "accepted"),
                            ("processing", "processing"),
                        ],
                        default="processing",
                        max_length=10,
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Название города",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Название города",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderedProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.IntegerField(default=1)),
                ("price", models.FloatField(default=1.01)),
                ("count", models.IntegerField(default=1)),
                ("date", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, null=True)),
                ("fullDescription", models.TextField(blank=True, null=True)),
                ("freeDelivery", models.BooleanField(blank=True, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                ("salePrice", models.FloatField(blank=True, null=True)),
                ("dateFrom", models.DateTimeField(blank=True, null=True)),
                ("dateTo", models.DateTimeField(blank=True, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orderedproduct_order",
                        to="order.order",
                    ),
                ),
                (
                    "reviews",
                    models.ManyToManyField(
                        blank=True,
                        related_name="ordredproduct_review",
                        to="review.review",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="ordredproduct_tag", to="tag.tag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "src",
                    models.ImageField(
                        default="app_users/orderedproducts/default.png",
                        upload_to="app_users/orderedproducts/",
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        default="Just an image", max_length=128, verbose_name="Описание"
                    ),
                ),
                (
                    "ordredproduct",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ordredproduct_images",
                        to="order.orderedproduct",
                        verbose_name="Linked to product:",
                    ),
                ),
            ],
            options={
                "verbose_name": "OrderImage",
                "verbose_name_plural": "OrderImages",
            },
        ),
    ]