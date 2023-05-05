from main_store.serializers import (
    ItemSerializer,
    PicturesSerializer,
    UserSerializer,
    BucketCreateSerializer,
    BuketSerializer,
    LikeCreateSerializer,
    LikeSerializer,
)
from main_store.models import Items, Pictures, User, Buket, Likes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from djoser.serializers import UserCreateSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


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
        user = serializer.save()

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