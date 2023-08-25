from rest_framework import serializers
from rest_framework.fields import IntegerField

from product.models import Image, Product
from review.models import Review
from specification.models import Specification
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


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ["name", "value"]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["author", "email", "text", "rate", "date"]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    tags = TagsSerializer(many=True)
    reviews = ReviewsSerializer(many=True)
    specifications = SpecificationSerializer(many=True)

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
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            "specifications",
            "reviews",
            "rating",
        ]
