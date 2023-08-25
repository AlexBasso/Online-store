from random import randrange
import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_user.models import Profile

# User = get_user_model()


# class SignUpView(APIView):
#
#     # def post(self, request: Request) -> Response:
#     #     serialized_data = list(request.POST.keys())[0]
#     #     user_data = json.loads(serialized_data)
#     #     name = user_data.get("name")
#     #     username = user_data.get("username")
#     #     password = user_data.get("password")
#
#     def post(self, request):
#         print('inside post!')
#         serialized_data = list(request.data.keys())[0]
#         user_data = json.loads(serialized_data)
#         name = user_data.get("name")
#         username = user_data.get("username")
#         password = user_data.get("password")
#
#         # try:
#         #     user = User.objects.create_user(username=username, password=password)
#         #     profile = Profile.objects.create(user=user, first_name=name)
#         #     user = authenticate(request, username=username, password=password)
#         #     if user is not None:
#         #         login(request, user)
#         #     return Response(status=status.HTTP_201_CREATED)
#         # except Exception:
#         #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#         try:
#             print('inside try')
#             print("username: {}, password: {}".format(username, password))
#             user = User.objects.create_user(username=username, password=password)
#             print('1')
#             profile = Profile.objects.create(user=user, first_name=name)
#             print('2')
#             user = authenticate(request, username=username, password=password)
#             print('3')
#             if user is not None:
#                 print('inside user is not None')
#                 login(request, user)
#             return Response(status=status.HTTP_201_CREATED)
#         except Exception:
#             print('inside except', Exception.args)
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def banners(request):
    data = [
        {
            "id": "123",
            "category": 55,
            "price": 500.67,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
                {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "any alt text",
                }
            ],
            "tags": ["string"],
            "reviews": 5,
            "rating": 4.6,
        },
    ]
    return JsonResponse(data, safe=False)


def categories(request):
    data = [
        {
            "id": 123,
            "title": "video card",
            "image": {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "Image alt string",
            },
            "subcategories": [
                {
                    "id": 123,
                    "title": "video card",
                    "image": {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "Image alt string",
                    },
                }
            ],
        }
    ]
    return JsonResponse(data, safe=False)


#
# def catalog(request):
# 	data = {
# 		 "items": [
# 				 {
# 					 "id": 123,
# 					 "category": 123,
# 					 "price": 500.67,
# 					 "count": 12,
# 					 "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
# 					 "title": "video card",
# 					 "description": "description of the product",
# 					 "freeDelivery": True,
# 					 "images": [
# 					 		{
# 					 			"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 					 			"alt": "hello alt",
# 							}
# 					 ],
# 					 "tags": [
# 					 		{
# 					 			"id": 0,
# 					 			"name": "Hello world"
# 					 		}
# 					 ],
# 					 "reviews": 5,
# 					 "rating": 4.6
# 				 }
# 		 ],
# 		 "currentPage": randrange(1, 4),
# 		 "lastPage": 3
# 	 }
# 	return JsonResponse(data)


def productsPopular(request):
    data = [
        {
            "id": "123",
            "category": 55,
            "price": 500.67,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
                {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "hello alt",
                }
            ],
            "tags": [{"id": 0, "name": "Hello world"}],
            "reviews": 5,
            "rating": 4.6,
        }
    ]
    return JsonResponse(data, safe=False)


def productsLimited(request):
    data = [
        {
            "id": "123",
            "category": 55,
            "price": 500.67,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
                {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "hello alt",
                }
            ],
            "tags": [{"id": 0, "name": "Hello world"}],
            "reviews": 5,
            "rating": 4.6,
        }
    ]
    return JsonResponse(data, safe=False)


def sales(request):
    data = {
        "items": [
            {
                "id": 123,
                "price": 500.67,
                "salePrice": 200.67,
                "dateFrom": "05-08",
                "dateTo": "05-20",
                "title": "video card",
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
            }
        ],
        "currentPage": randrange(1, 4),
        "lastPage": 3,
    }
    return JsonResponse(data)


def basket(request):
    if request.method == "GET":
        print("[GET] /api/basket/")
        data = [
            {
                "id": 123,
                "category": 55,
                "price": 500.67,
                "count": 12,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            },
            {
                "id": 124,
                "category": 55,
                "price": 201.675,
                "count": 5,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            },
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        id = body["id"]
        count = body["count"]
        print(
            "[POST] /api/basket/   |   id: {id}, count: {count}".format(
                id=id, count=count
            )
        )
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500.67,
                "count": 13,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            }
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        body = json.loads(request.body)
        id = body["id"]
        print("[DELETE] /api/basket/")
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500.67,
                "count": 11,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [{"id": 0, "name": "Hello world"}],
                "reviews": 5,
                "rating": 4.6,
            }
        ]
        return JsonResponse(data, safe=False)


# def signIn(request):
# 	if request.method == "POST":
# 		body = json.loads(request.body)
# 		username = body['username']
# 		password = body['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return HttpResponse(status=200)
# 		else:
# 			return HttpResponse(status=500)

# def signUp(request):
# 	user = User.objects.create_user("mir232", "lennon@thebeatles.com", "pass232")
# 	user.save()
# 	return HttpResponse(status=200)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)


def product(request, id):
    data = {
        "id": 123,
        "category": 55,
        "price": 500.67,
        "count": 12,
        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        "title": "video card",
        "description": "description of the product",
        "fullDescription": "full description of the product",
        "freeDelivery": True,
        "images": [
            {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "hello alt",
            }
        ],
        "tags": [{"id": 0, "name": "Hello world"}],
        "reviews": [
            {
                "author": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "text": "rewrewrwerewrwerwerewrwerwer",
                "rate": 4,
                "date": "2023-05-05 12:12",
            }
        ],
        "specifications": [{"name": "Size", "value": "XL"}],
        "rating": 4.6,
    }
    return JsonResponse(data)


def tags(request):
    data = [
        {"id": 0, "name": "tag0"},
        {"id": 1, "name": "tag1"},
        {"id": 2, "name": "tag2"},
    ]
    return JsonResponse(data, safe=False)


def productReviews(request, id):
    data = [
        {
            "author": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "text": "rewrewrwerewrwerwerewrwerwer",
            "rate": 4,
            "date": "2023-05-05 12:12",
        },
        {
            "author": "2Annoying Orange",
            "email": "no-reply@mail.ru",
            "text": "rewrewrwerewrwerwerewrwerwer",
            "rate": 5,
            "date": "2023-05-05 12:12",
        },
    ]
    return JsonResponse(data, safe=False)


# def profile(request):
# 	if(request.method == 'GET'):
# 		data = {
# 			"fullName": "Annoying Orange",
# 			"email": "no-reply@mail.ru",
# 			"phone": "88002000600",
# 			"avatar": {
# 				"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 				"alt": "hello alt",
# 			}
# 		}
# 		return JsonResponse(data)
#
# 	elif(request.method == 'POST'):
# 		data = {
# 			"fullName": "Annoying Green",
# 			"email": "no-reply@mail.ru",
# 			"phone": "88002000600",
# 			"avatar": {
# 				"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 				"alt": "hello alt",
# 			}
# 		}
# 		return JsonResponse(data)
#
# 	return HttpResponse(status=500)
#
# def profilePassword(request):
# 	return HttpResponse(status=200)


def orders(request):
    if request.method == "GET":
        data = [
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string",
                            }
                        ],
                        "tags": [{"id": 12, "name": "Gaming"}],
                        "reviews": 5,
                        "rating": 4.6,
                    }
                ],
            },
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string",
                            }
                        ],
                        "tags": [{"id": 12, "name": "Gaming"}],
                        "reviews": 5,
                        "rating": 4.6,
                    }
                ],
            },
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = {
            "orderId": 123,
        }
        return JsonResponse(data)

    return HttpResponse(status=500)


def order(request, id):
    if request.method == "GET":
        data = {
            "id": 123,
            "createdAt": "2023-05-05 12:12",
            "fullName": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "phone": "88002000600",
            "deliveryType": "free",
            "paymentType": "online",
            "totalCost": 567.8,
            "status": "accepted",
            "city": "Moscow",
            "address": "red square 1",
            "products": [
                {
                    "id": 123,
                    "category": 55,
                    "price": 500.67,
                    "count": 12,
                    "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                    "title": "video card",
                    "description": "description of the product",
                    "freeDelivery": True,
                    "images": [
                        {
                            "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                            "alt": "Image alt string",
                        }
                    ],
                    "tags": [{"id": 12, "name": "Gaming"}],
                    "reviews": 5,
                    "rating": 4.6,
                },
            ],
        }
        return JsonResponse(data)

    elif request.method == "POST":
        data = {"orderId": 123}
        return JsonResponse(data)

    return HttpResponse(status=500)


def payment(request, id):
    print("qweqwewqeqwe", id)
    return HttpResponse(status=200)


# def avatar(request):
# 	if request.method == "POST":
# # 		print(request.FILES["avatar"])
# 		return HttpResponse(status=200)
