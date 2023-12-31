# Generated by Django 4.2 on 2023-08-11 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("review", "0001_initial"),
        ("tag", "0001_initial"),
        ("specification", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                    "reviews",
                    models.ManyToManyField(
                        blank=True, related_name="product_review", to="review.review"
                    ),
                ),
                (
                    "specifications",
                    models.ManyToManyField(
                        blank=True,
                        related_name="product_specification",
                        to="specification.specification",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="product_tag", to="tag.tag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                        default="app_users/products/default.png",
                        upload_to="app_users/products/",
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
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="product.product",
                        verbose_name="Linked to product:",
                    ),
                ),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
            },
        ),
    ]
