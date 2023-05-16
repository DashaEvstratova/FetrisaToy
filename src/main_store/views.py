from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password

from main_store.serializers import (
    ItemSerializer,
    PicturesSerializer,
    UserSerializer,
    BucketCreateSerializer,
    BuketSerializer,
    LikeCreateSerializer,
    LikeSerializer,
)
from main_store.models import Items, Pictures, User, Buket, Likes, Orders, OrederData
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from djoser.serializers import UserCreateSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
import jwt
from django.conf import settings
from django.core.mail import send_mail


@method_decorator(csrf_exempt, name="dispatch")
class ResetPasswordView(View):
    def post(self, request):
        email = list(request.POST.keys())

        # Проверка наличия пользователя с указанным email
        try:
            user = User.objects.get(email=email[0])
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)

        # Генерация JWT-токена
        payload = {"email": email[0]}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        # Сохранение токена сброса пароля в модели пользователя
        user.reset_token = token
        user.save()

        # Формирование ссылки для сброса пароля
        reset_url = f"http://localhost:8080/reset-password/{token}"

        # Отправка письма со ссылкой на сброс пароля
        subject = "Сброс пароля"
        message = f"Нажмите на ссылку ниже:\n\n{reset_url}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email[0]])

        return JsonResponse({"message": "Email sent"})


@csrf_exempt
def reset_password_api(request, token):
    if request.method == "POST":
        password = list(request.POST.keys())[0]
        try:
            user = User.objects.get(reset_token=token)
        except User.DoesNotExist:
            return JsonResponse({"error": "Недействительный токен сброса пароля."}, status=400)

        # Изменяем пароль пользователя
        user.password = make_password(password)
        user.reset_token = None  # Опционально: очищаем поле с токеном сброса пароля
        user.save()

        # Пример успешного ответа
        response = {"message": "Пароль успешно сброшен."}
        return JsonResponse(response)

    # Если метод запроса не POST, возвращаем ошибку
    return JsonResponse({"error": "Метод запроса не разрешен."}, status=405)


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        file = request.FILES["file"]
        user_data = request.POST.get("user")  # Получение данных о пользователе
        pk = json.loads(user_data)
        user = User.objects.get(pk=pk)
        setattr(user, "avatar", file)
        user.save()
        return HttpResponse("Файл успешно загружен")


class UserUpdateAPIView(APIView):
    def put(self, request, pk):
        # Получаем данные из запроса
        parameter = request.data.get("parameter")
        value = request.data.get("value")

        # Проверяем, что параметр и значение переданы
        if not parameter or not value:
            return Response({"error": "Необходимо указать параметр и значение."}, status=status.HTTP_400_BAD_REQUEST)

        # Находим пользователя по его идентификатору
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        # Обновляем соответствующее поле
        setattr(user, parameter, value)
        user.save()

        return Response({"message": "Параметр успешно обновлен."}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Получаем данные из запроса
        items = data.get("items")
        total = data.get("total")
        user_id = data.get("user")
        user = User.objects.get(id=user_id)
        # Создаем новый заказ и сохраняем его в базе данных
        order = Orders.objects.create(client=user, sum_of_order=total)

        # Сохраняем данные о товарах в заказе
        for item in items:
            item_id = Items.objects.get(id=item["id"])
            OrederData.objects.create(item=item_id, count=item["count"], order=order)

        # Удаляем товары из корзины
        item_ids = [item["id"] for item in items]
        Buket.objects.filter(item__id__in=item_ids).delete()

        return JsonResponse({"success": True, "order_id": order.id})

    return JsonResponse({"success": False})


class CheckBucketItemAPI(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        item_id = request.GET.get("item_id")

        try:
            bucket = Buket.objects.get(user_id=user_id, item_id=item_id)
            count = bucket.count
            return Response({"count": count}, status=status.HTTP_200_OK)
        except Buket.DoesNotExist:
            return Response({"exists": False}, status=status.HTTP_200_OK)


class CheckLikeItemAPI(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        item_id = request.GET.get("item_id")

        try:
            like = Likes.objects.get(user_id=user_id, item_id=item_id)
            return Response({"exists": True}, status=status.HTTP_200_OK)
        except Buket.DoesNotExist:
            return Response({"exists": False}, status=status.HTTP_200_OK)


class RemoveLikeAPI(APIView):
    def delete(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        item_id = request.GET.get("item_id")

        try:
            like = Likes.objects.get(user_id=user_id, item_id=item_id)
            like.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Likes.DoesNotExist:
            return Response({"success": False}, status=status.HTTP_404_NOT_FOUND)


class RemoveBuketAPI(APIView):
    def delete(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        item_id = request.GET.get("item_id")

        try:
            buket = Buket.objects.get(user_id=user_id, item_id=item_id)
            buket.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Likes.DoesNotExist:
            return Response({"success": False}, status=status.HTTP_404_NOT_FOUND)


class UpdateBucketItemAPI(APIView):
    def put(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        item_id = request.data.get("item_id")
        count = request.data.get("count")

        try:
            bucket = Buket.objects.get(user_id=user_id, item_id=item_id)
            bucket.count = count
            bucket.save()

            return Response({"message": "Bucket item updated successfully."}, status=status.HTTP_200_OK)
        except Buket.DoesNotExist:
            return Response({"message": "Bucket item does not exist."}, status=status.HTTP_404_NOT_FOUND)


class ItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        return PicturesSerializer

    def get_queryset(self):
        return Pictures.objects.filter(item__isnull=False, item__category="Игрушки").prefetch_related("item")


class PatternViewSet(ModelViewSet):
    def get_serializer_class(self):
        return PicturesSerializer

    def get_queryset(self):
        return Pictures.objects.filter(item__isnull=False, item__category="Выкройка").prefetch_related("item")


class AllItemViewSet(RetrieveAPIView):
    serializer_class = PicturesSerializer
    queryset = Pictures.objects.filter(item__isnull=False)
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs["id"])


class RegistrationView(APIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Создаем пользователя и устанавливаем поле is_active в True
        user = serializer.save(is_active=True)

        token_data = TokenObtainPairSerializer().get_token(user)
        token = str(token_data.access_token)
        refresh_token = str(token_data)

        return Response(
            {"user_id": user.id, "email": user.email, "token": token, "refresh_token": refresh_token},
            status=status.HTTP_201_CREATED,
        )


class JWTTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairSerializer
    token_refresh = None


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@api_view(["POST"])
def bucket_create_view(request):
    serializer = BucketCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})
    else:
        return Response(serializer.errors, status=400)


class BuketList(generics.ListAPIView):
    serializer_class = BuketSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        queryset = Buket.objects.filter(user_id=user_id)
        return queryset


@api_view(["POST"])
def like_create_view(request):
    serializer = LikeCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})
    else:
        return Response(serializer.errors, status=400)


class LikeList(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        queryset = Likes.objects.filter(user_id=user_id)
        return queryset
