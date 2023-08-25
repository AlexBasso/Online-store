import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_user.models import Profile, Avatar
from auth_user.serializers import ProfileSerializer


class SignInView(APIView):
    def post(self, request: Request) -> Response:
        # print('\n\nPrinting keys: ', list(request.POST.keys()))
        # print('\n\nPrinting keys: ', list(request.POST.keys())[0])
        serialized_data = list(request.POST.keys())[0]
        user_data = json.loads(serialized_data)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)
        print("\nUser: ", user)

        if user is not None:
            print("before user is smth response")
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        print("before user is None response")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):
    def post(self, request: Request) -> Response:
        print("inside post!")
        serialized_data = list(request.data.keys())[0]
        user_data = json.loads(serialized_data)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        try:
            print("inside try")
            print(
                "username: {}, password: {}, name: {}".format(username, password, name)
            )
            user = User.objects.create_user(username=username, password=password)
            print("1")
            profile = Profile.objects.create(user=user, fullName=name)
            print("profile: ", profile)
            print("2")
            user = authenticate(request, username=username, password=password)
            print("3")
            if user is not None:
                print("inside user is not None")
                login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            print("inside except", Exception.args)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(("POST",))
def signOut(request: Request) -> Response:
    print("in logout")
    logout(request)
    print("logout complete")
    return Response(status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        print("inside get")
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        # print('\nprinting get auth:\n', serializer.data)
        print("finished get")
        return Response(serializer.data)

    # 		data = {
    # 			"fullName": "Annoying Orange",
    # 			"email": "no-reply@mail.ru",
    # 			"phone": "88002000600",
    # 			"avatar": {
    # 				"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    # 				"alt": "hello alt",
    # 			}
    # 		}

    def post(self, request: Request) -> Response:
        print("inside post")
        print("request.data: ", request.data)
        profile = Profile.objects.get(user=request.user)
        print("profile: ", profile)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        print("serializer: ", serializer)

        if serializer.is_valid(raise_exception=True):
            print("serializer is valid")
            serializer.save()
            return Response(serializer.data)
        print("serializer is not valid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(("POST",))
    def avatar(request: Request) -> Response:
        print("inside post avatar")
        if request.method == "POST":
            print("inside avatar")
            avatar, created = Avatar.objects.get_or_create(src=request.FILES["avatar"])
            request.user.profile.avatar = avatar
            request.user.profile.save()
            print("after save")
            return Response(status=200)


class ProfilePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(("POST",))
    def profile_password(request: Request) -> Response:
        print("inside profile_password")
        user = User.objects.get(username=request.user)
        if check_password(request.data["currentPassword"], user.password):
            print("check success")
            user.set_password(request.data["newPassword"])
            user.save()
            return Response(status=200)
        print("check failed")
        return Response(status=status.HTTP_401_UNAUTHORIZED)
