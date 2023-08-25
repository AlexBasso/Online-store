import random

from django.utils import timezone

# This is needed! Do not DELETE import of Count!
from django.db.models import Count

from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from catalog.models import CatalogItems, CatalogItem, SalesItem
from catalog.serializers import (
    ProductShortSerializer,
    CatalogItemsSerializer,
    CatalogItemSerializer,
    SalesItemSerializer,
)
from product.models import Product


class BannersView(APIView):
    """Баннер, первый продукт который виден на сайте. Без понятия как его выбирать, поэтому поставил рандом"""

    def get(self, request: Request) -> JsonResponse:
        items = list(Product.objects.all())
        random_items = random.sample(items, 1)[0]
        # print('\n\nprinting random_items: \n\n', random_items)
        serializer = ProductShortSerializer(random_items)
        # print('\n\nprinting serializer: \n\n', serializer)
        final_data = [serializer.data]
        # print('\n\nprinting final_data: \n\n', final_data)

        return JsonResponse(final_data, safe=False)


class CategoriesView(APIView):
    """Категории и подкатегории, отоброжаются на главной странице, вложеность 2"""

    def get(self, request: Request) -> JsonResponse:
        catalogitems = CatalogItems.objects.all()
        serializer = CatalogItemsSerializer(catalogitems, many=True)
        final_data = serializer.data
        # print('\n\nprinting cat final_data: \n\n', final_data)

        return JsonResponse(final_data, safe=False)


class CatalogView(APIView):
    def get(self, request: Request) -> JsonResponse:
        command = (
            "Product.objects.filter("
            "price__range=[request.query_params['filter[minPrice]'], request.query_params['filter[maxPrice]']]"
        )
        # print('\nprinting reuqest.query_params: \n', request.query_params)
        temp_dict = dict(request.query_params.lists())
        # print('\nprinting filter minPrice: \n', request.query_params['filter[minPrice]'],
        #       type(request.query_params['filter[minPrice]']))
        # print('what is name param: ', request.query_params['filter[name]'])

        # 1 name
        if request.query_params["filter[name]"] != "":
            command += ", name=request.query_params['filter[name]']"

        freedelivery_value = (
            True
            if request.query_params["filter[freeDelivery]"].lower() == "true"
            else False
        )
        # print('printing freedelivery_value: ', freedelivery_value)

        # 2 free delivery
        if freedelivery_value:
            command += ", freeDelivery=True"

        # 3 available
        available = (
            True
            if request.query_params["filter[available]"].lower() == "true"
            else False
        )
        # print('is it available? ', request.query_params['filter[available]'], 'and param sais: ', available)

        if available:
            command += ", count__gt=0"

        # 4 category
        if "category" in request.query_params:
            # print('yescategor is here', request.query_params['category'])
            command += ", category=request.query_params['category']"
        else:
            print("Not category its not here")

        # closing filter
        command += ")"

        # 5 tags
        if "tags[]" in request.query_params:
            print("yes tags are here ", request.query_params["tags[]"])
            for elem in temp_dict["tags[]"]:
                command += ".filter(tags__id={})".format(elem)
            print("printing command after tags: ", command)
        else:
            print("Tags are not here")

        # 6 sorting
        # print('printing sorting: ', request.query_params['sort'])
        # print('printing sorting: ', request.query_params['sortType'])
        if request.query_params["sortType"] == "dec":
            print("it is dec")
            if request.query_params["sort"] == "reviews":
                print("it is rev")
                # .annotate(num_participants=Count('participants'))
                command += ".annotate(num_rev=Count('reviews')).order_by('-num_rev')"
            else:
                command += ".order_by('-{0}')".format(request.query_params["sort"])
        else:
            print("it is inc")
            if request.query_params["sort"] == "reviews":
                print("it is rev")
                command += ".annotate(num_rev=Count('reviews')).order_by('num_rev')"
            else:
                command += ".order_by('{0}')".format(request.query_params["sort"])

        print("\n\nprinting command:", command, "\n\n")
        items = eval(command)
        # print('printing items: ', items)

        page = Paginator(items, 2)
        # print('printing page: ', page)
        # print('printing page.page_range: ', page.page_range)
        # print('printing page.object_list: ', page.object_list)
        requested_page = page.page(request.query_params["currentPage"])
        # print('printing requested_page: ', requested_page)
        # print('printing requested_page.page_range: ', requested_page.page_range)
        # print('printing requested_page.object_list: ', requested_page.object_list)
        catalog_item = CatalogItem
        catalog_item.items = requested_page.object_list
        catalog_item.currentPage = int(request.query_params["currentPage"])
        catalog_item.lastPage = page.num_pages

        # print('\n\nprinting catalog item: \n\n', catalog_item)

        final_data = CatalogItemSerializer(catalog_item)
        # print(final_data.data)

        return JsonResponse(final_data.data)


class ProductsPopularView(APIView):
    """Популярный продукт, виден на первой странице сайта. Без понятия как его/их выбирать, поэтому поставил рандом"""

    def get(self, request: Request) -> JsonResponse:
        items = list(Product.objects.all())
        random_items = random.sample(items, 1)[0]
        serializer = ProductShortSerializer(random_items)
        final_data = [serializer.data]

        return JsonResponse(final_data, safe=False)


class ProductsLimitedView(APIView):
    """Лимитированый продукт, виден на первой странице сайта. Без понятия как его/их выбирать, поэтому поставил рандом"""

    def get(self, request: Request) -> JsonResponse:
        items = list(Product.objects.all())
        random_items = random.sample(items, 1)[0]
        serializer = ProductShortSerializer(random_items)
        final_data = [serializer.data]

        return JsonResponse(final_data, safe=False)


class SalesView(APIView):
    """Распродажа продуктов, виден на первой странице сайта. Без понятия как его/их выбирать, поэтому поставил рандом"""

    def get(self, request: Request) -> JsonResponse:
        print("inside Sales get")
        items = list(
            Product.objects.filter(
                dateFrom__lte=timezone.now(), dateTo__gte=timezone.now()
            )
        )
        print("printing items: ", items)

        page = Paginator(items, 2)
        requested_page = page.page(request.query_params["currentPage"])

        sale_item = SalesItem
        sale_item.items = requested_page.object_list
        sale_item.currentPage = int(request.query_params["currentPage"])
        sale_item.lastPage = page.num_pages

        final_data = SalesItemSerializer(sale_item)
        print("printing final_data.data: ", final_data.data)
        return JsonResponse(final_data.data)
