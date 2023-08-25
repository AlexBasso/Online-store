from django.contrib.auth.models import User

from rest_framework import serializers

from basket.models import OrderProduct, Basket
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


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["count", "product"]


class BasketSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Basket
        fields = ["products"]

    def create(self, validated_data):
        print("INSIDE CREATE!!!")
        products_data = validated_data.pop("products")
        basket = Basket.objects.create(**validated_data)
        OrderProduct.objects.create(basket=basket, **products_data)
        return basket

    def update(self, instance, validated_data):
        print("\n-------------------------------------------")
        print("inside UPDATE serializer\n")
        # print('printing validated_data: ', validated_data)
        # print('printing instance: ', instance)
        # print('printing instance.products.all(): ', instance.products.all())
        # print('printing instance TESTING: ', instance.products.first())

        products_data = validated_data.pop("products")
        # print('\nprinting products_data: ', products_data, type(products_data))
        # print('\nprinting products_data[0]: ', products_data[0], type(products_data[0]))
        # print('printing products_data[0]["count"]: ', products_data[0]["count"], type(products_data[0]["count"]))
        # print('printing products_data[0]["product"]: ', products_data[0]["product"], type(products_data[0]["product"]))
        # print('printing products_data[0]["product"].id: ', products_data[0]["product"].id, type(products_data[0]["product"].id))

        products = instance.products.all()
        # print('\n\n---printing products: ', products)
        list_product_id = []
        for orderproduct in products:
            # print('printing orderproduct.id: ', orderproduct.id)
            # print('printing orderproduct.product.id: ', orderproduct.product.id)
            list_product_id.append(orderproduct.product.id)
        # print('\n--printing list_product_id: ', list_product_id)

        if products_data[0]["product"].id in list_product_id:
            # print('\nProduct is already in basket!')
            current_order_product_to_be_updated = OrderProduct.objects.get(
                product__id=products_data[0]["product"].id, basket_orderproduct=instance
            )
            # print('printing current_order_product_to_be_updated: ', current_order_product_to_be_updated)
            # print('printing current_order_product_to_be_updated.count BEFORE: ', current_order_product_to_be_updated.count)
            # print('\nprinting products_data[0]["count"]: ', products_data[0]["count"], type(products_data[0]["count"]))
            if products_data[0]["count"] != 0:
                current_order_product_to_be_updated.count = products_data[0]["count"]
                # print('printing current_order_product_to_be_updated.count AFTER: ', current_order_product_to_be_updated.count)
                current_order_product_to_be_updated.save()
            else:
                # print('DELETING current_order_product_to_be_updated!!!')
                current_order_product_to_be_updated.delete()

        else:
            # print('\nProduct is NOT in basket!')
            got_product = Product.objects.get(id=products_data[0]["product"].id)
            product_to_add = OrderProduct.objects.create(
                count=products_data[0]["count"], product=got_product
            )
            # print('printing product_to_add: ', product_to_add)
            # print('printing product_to_add.id: ', product_to_add.id)
            list_order_product_id = []
            for orderproduct in products:
                # print('printing orderproduct.id: ', orderproduct.id)
                list_order_product_id.append(orderproduct.id)
            # print('\n--printing list_order_product_id: ', list_order_product_id)

            list_order_product_id.append(product_to_add.id)

            # print('\nprinting list_order_product_id final: ', list_order_product_id)
            new_to_add_order_query = OrderProduct.objects.filter(
                id__in={order_product_id for order_product_id in list_order_product_id}
            )
            # print('printing new_to_add_order_query: ', new_to_add_order_query)
            instance.products.set(new_to_add_order_query)
            # print('instance.products: ', instance.products.all())
        instance.save()

        return instance
