import json
from collections import OrderedDict

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from basket.models import Basket, OrderProduct
from basket.serializers import BasketSerializer, ProductShortSerializer
from product.models import Product


class BasketView(APIView):
    def get(self, request: Request) -> JsonResponse:
        print("\ninside basket get")
        try:
            user = Basket.objects.get(user=request.user)
        except:
            user = Basket.objects.create(user=request.user)
            print("basket for user was created!")

        basket_serializer = BasketSerializer(user)
        basket_products = []
        for products in basket_serializer.data.values():
            # print('\nproducts: ', products)
            for product in products:
                buying_count = 0
                buying_product_id = 0
                for keys, values in product.items():
                    if keys == "count":
                        buying_count = values

                    elif keys == "product":
                        buying_product_id = values
                    else:
                        print("sadly nothing found")
                product = Product.objects.get(id=buying_product_id)
                product_serilizer = ProductShortSerializer(product)
                basket_product = product_serilizer.data
                basket_product["count"] = buying_count
                basket_products.append(basket_product)

        print("[GET] /api/basket/")
        return JsonResponse(basket_products, safe=False)

    def post(self, request: Request) -> JsonResponse:
        print("\ninside basket post\n")
        body = request.data
        id = body["id"]
        count = body["count"]
        # print('printing count: ', count, type(count))
        print(
            "[POST] /api/basket/   |   id: {id}, count: {count}\n".format(
                id=id, count=count
            )
        )

        try:
            users_basket = Basket.objects.get(user=request.user)
        except:
            users_basket = Basket.objects.create(user=request.user)
            print("basket for user was created!")
        # print('printing users_basket: ', users_basket)
        users_basket_serializer = BasketSerializer(users_basket)

        users_basket_serializer_data = users_basket_serializer.data
        # print('printing users_basket_serializer.data: ', users_basket_serializer_data)

        # Getting Product from OrderProduct:
        produdct_to_check = OrderProduct.objects.filter(
            product__id=id, basket_orderproduct=users_basket
        )
        # print('printing produdct_to_check: ', produdct_to_check)
        if produdct_to_check:
            count = produdct_to_check[0].count + int(count)
        # print('printing count AFTER UPDATE: ', count, type(count))

        # # # test 1    -   alternative OrderProduct creation
        product_to_add = OrderedDict()
        product_to_add["count"] = count
        product_to_add["product"] = id
        # print('printing product_to_add: ', product_to_add)

        # users_basket_serializer_data['products'].append(product_to_add)
        users_basket_serializer_data["products"] = [product_to_add]
        # print('printing users_basket_serializer.data: ', users_basket_serializer_data)

        serialier = BasketSerializer(users_basket, data=users_basket_serializer_data)

        if serialier.is_valid():
            print("it is valid")
            serialier.save()
        else:
            print("it is not valid")

        # print('\n\nprinting serialier.data: ', serialier.data)
        final_data = serialier.data["products"]
        # print('\n\nprinting final_data: ', final_data, type(final_data))
        response = []
        for elem in final_data:
            # print('\nprinting elem["product"]: ', elem["product"])
            product = Product.objects.get(id=elem["product"])
            # print('printing product: ', product)
            product_serilizer = ProductShortSerializer(product)
            # print('printing product_serilizer: ', product_serilizer)
            # print('printing product_serilizer.data: ', product_serilizer.data)
            product_serilizer_data = product_serilizer.data
            product_serilizer_data["count"] = elem["count"]
            # print('printing product_serilizer_data["count"]: ', product_serilizer_data["count"])

            response.append(product_serilizer_data)

        # print("\n\nPrinting response: ", response)

        return JsonResponse(response, safe=False)

    def delete(self, request: Request) -> JsonResponse:
        print("Inside DELETE")
        body = json.loads(request.body)
        # print('printing body: ', body)
        id = body["id"]
        count = body["count"]
        print("[DELETE] /api/basket/\n")

        try:
            users_basket = Basket.objects.get(user=request.user)
        except:
            users_basket = Basket.objects.create(user=request.user)
            print("basket for user was created!")
        users_basket_serializer = BasketSerializer(users_basket)
        users_basket_serializer_data = users_basket_serializer.data
        # print('printing users_basket_serializer.data: ', users_basket_serializer_data)

        produdct_to_check = OrderProduct.objects.filter(
            product__id=id, basket_orderproduct=users_basket
        )
        # print('printing produdct_to_check: ', produdct_to_check)
        # print('printing produdct_to_check.count: ', produdct_to_check[0].count)
        count = produdct_to_check[0].count - int(count)
        # print('printing count AFTER UPDATE: ', count, type(count))
        if count < 0:
            count = 0

        # # # test 1    -   alternative OrderProduct creation
        product_to_delete = OrderedDict()
        product_to_delete["count"] = count
        product_to_delete["product"] = id
        # print('printing product_to_add: ', product_to_delete)

        # users_basket_serializer_data['products'].append(product_to_add)
        users_basket_serializer_data["products"] = [product_to_delete]
        # print('printing users_basket_serializer.data: ', users_basket_serializer_data)

        serialier = BasketSerializer(users_basket, data=users_basket_serializer_data)

        if serialier.is_valid():
            print("it is valid")
            serialier.save()
        else:
            print("it is not valid")

        # print('\n\nprinting serialier.data: ', serialier.data)
        final_data = serialier.data["products"]
        # print('\n\nprinting final_data: ', final_data, type(final_data))
        response = []
        for elem in final_data:
            # print('\nprinting elem["product"]: ', elem["product"])
            product = Product.objects.get(id=elem["product"])
            # print('printing product: ', product)
            product_serilizer = ProductShortSerializer(product)
            # print('printing product_serilizer: ', product_serilizer)
            # print('printing product_serilizer.data: ', product_serilizer.data)
            product_serilizer_data = product_serilizer.data
            product_serilizer_data["count"] = elem["count"]
            # print('printing product_serilizer_data["count"]: ', product_serilizer_data["count"])

            response.append(product_serilizer_data)

        # print("\n\nPrinting response: ", response)

        return JsonResponse(response, safe=False)
