from rest_framework import serializers

from order.models import OrderedProduct, Order
from product.models import Image
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


class OrderedProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source="ordredproduct_images", read_only=True, many=True)
    tags = TagsSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = OrderedProduct
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


class OrderSerializer(serializers.ModelSerializer):
    products = OrderedProductSerializer(
        source="orderedproduct_order", read_only=True, many=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "address",
            "products",
        ]
