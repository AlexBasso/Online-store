from django.http import JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_user.models import Profile
from order.models import OrderedProduct, Order, OrderImage
from order.serializers import OrderSerializer
from product.models import Product
from tag.models import Tag


class OrdersView(APIView):
    def get(self, request: Request) -> JsonResponse:
        print("INSIDE ORDERS GET")
        print("\nprinting request: ", request.user)

        orders = Order.objects.filter(user=request.user)
        print(orders)

        serializer = OrderSerializer(orders, many=True)
        print("printing serializer.data:", serializer.data)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request: Request) -> JsonResponse:
        print("INSIDE ORDERS POST")
        request_data = request.data
        ordered_products = []
        for product in request_data:
            product_id = product.pop("id")
            temp_images = product.pop("images")
            temp_tags = product.pop("tags")
            product.pop("reviews")

            ordered_product = OrderedProduct.objects.create(**product)
            # print('\nprinting new ordered_product: ', ordered_product, type(ordered_product))

            list_of_temp_images = []
            for dict_image in temp_images:
                dict_image["src"] = dict_image["src"][6:]
                temp_image = OrderImage.objects.create(**dict_image)
                list_of_temp_images.append(temp_image)
            ordered_product.ordredproduct_images.set(list_of_temp_images)

            for dict_tags in temp_tags:
                print("\nprinting temp_tag: ", dict_tags, type(dict_tags))
                ordered_product.tags.add(Tag.objects.get(id=dict_tags["id"]))

            temp_reviews = Product.objects.get(id=product_id).reviews.all()
            ordered_product.reviews.set(temp_reviews)

            ordered_products.append(ordered_product)

        user_order = Order.objects.create(user=request.user)
        user_order.orderedproduct_order.set(ordered_products)

        profile = Profile.objects.get(user=request.user)
        products_for_total = user_order.orderedproduct_order.all()
        total_summ = 0
        for product in products_for_total:
            temp_summ = product.price * product.count
            total_summ += temp_summ
        totalCost = round(total_summ, 2)
        test_data = {
            "fullName": profile.fullName,
            "email": profile.email,
            "phone": profile.phone,
            "totalCost": totalCost,
        }

        serializer = OrderSerializer(user_order, data=test_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error_messages)
            print(serializer.errors)
        # print('\nprinting user_order: ', user_order)

        data = {
            "orderId": user_order.id,
        }
        return JsonResponse(data)


class OrderView(APIView):
    def get(self, request: Request, id) -> JsonResponse:
        print("inside OrderView get")
        print("printing ID: ", id)

        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        serialized_data = serializer.data
        # print('\nprinting serialized_data: ', serialized_data)

        return JsonResponse(serialized_data)

    def post(self, request: Request, id) -> JsonResponse:
        print("inside OrderView post")
        # print('printing request.data: ', request.data)
        request_data = request.data
        request_data["status"] = "accepted"
        order = Order.objects.get(id=id)

        updated_order = OrderSerializer(order, data=request_data)
        if updated_order.is_valid():
            updated_order.save()
        else:
            print(updated_order.error_messages)
            print(updated_order.errors)

        # print('\n\nprinting updated_order: ', updated_order)
        data = {"orderId": order.id}
        return JsonResponse(data)


class PaymentView(APIView):
    def post(self, request: Request, id) -> Response:
        print("ID: ", id)
        # print('request.data: ', request.data)
        # print('request.data["number"]: ', request.data["number"], type(request.data["number"]))
        # print('request.data["year"]: ', request.data["year"], type(request.data["year"]))
        # print('request.data["month"]: ', request.data["month"], type(request.data["month"]))
        # print('request.data["code"]: ', request.data["code"], type(request.data["code"]))
        data_is_not_valid = False
        if len(request.data["number"]) != 16 or (
            request.data["number"].isnumeric() is not True
        ):
            data_is_not_valid = True
        if len(request.data["year"]) != 2 or (
            request.data["year"].isnumeric() is not True
        ):
            data_is_not_valid = True
        if (
            len(request.data["month"]) != 2
            or (request.data["month"].isnumeric() is not True)
            or (0 < int(request.data["month"]) < 13) is not True
        ):
            data_is_not_valid = True
        if len(request.data["code"]) != 3 or (
            request.data["code"].isnumeric() is not True
        ):
            data_is_not_valid = True
        print("data_is_not_valid: ", data_is_not_valid)
        if data_is_not_valid:
            return Response(status=400)
        else:
            return Response(status=200)
