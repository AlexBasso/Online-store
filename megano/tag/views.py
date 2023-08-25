from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from tag.models import Tag
from tag.serializers import TagSerializer


class TagView(APIView):
    def get(self, request: Request) -> JsonResponse:
        items = Tag.objects.all()
        # print('\nprinting items tagsssssssssss:', items, type(items))
        serializer = TagSerializer(items, many=True)
        # print('\nprinting items tags serializer: ', serializer)
        # print('\nprinting items tags serializer.data: ', serializer.data)

        # data = [
        #     { "id": 0, "name": 'tag0' },
        #     { "id": 1, "name": 'tag1' },
        #     { "id": 2, "name": 'tag2' },
        # ]

        return JsonResponse(serializer.data, safe=False)
