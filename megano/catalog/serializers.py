from rest_framework import serializers

from catalog.models import CatalogItems, CatalogItem, SalesItem
from product.models import Image, Product
from tag.models import Tag


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ProductShortSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    tags = TagsSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        ]

    def get_reviews(self, obj):
        return obj.reviews.count()

    def get_rating(self, obj):
        return obj.reviews.count()


class SubCategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)

    class Meta:
        model = CatalogItems
        fields = ["id", "title", "image"]


class CatalogItemsSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    subcategories = SubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = CatalogItems
        fields = ["id", "title", "image", "subcategories"]


class CatalogItemSerializer(serializers.ModelSerializer):
    items = ProductShortSerializer(read_only=True, many=True)

    class Meta:
        model = CatalogItem
        fields = ["items", "currentPage", "lastPage"]


class SaleProductShortSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    dateFrom = serializers.DateTimeField(format="%m-%d")
    dateTo = serializers.DateTimeField(format="%m-%d")

    class Meta:
        model = Product
        fields = ["id", "price", "salePrice", "dateFrom", "dateTo", "title", "images"]


class SalesItemSerializer(serializers.ModelSerializer):
    items = SaleProductShortSerializer(read_only=True, many=True)

    class Meta:
        model = SalesItem
        fields = ["items", "currentPage", "lastPage"]
