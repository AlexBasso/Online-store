from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer, ReviewsSerializer


class ProductView(APIView):
    def get(self, request: Request, id) -> JsonResponse:
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)

        return JsonResponse(serializer.data)


class ProductReviewsView(APIView):
    def post(self, request: Request, id) -> JsonResponse:
        product = Product.objects.get(pk=id)

        data = ReviewsSerializer(data=request.data)
        if data.is_valid():
            data = data.data
            product.reviews.create(
                author=data["author"],
                email=data["email"],
                text=data["text"],
                rate=data["rate"],
            )
            return JsonResponse(data, safe=False)

        return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST)
