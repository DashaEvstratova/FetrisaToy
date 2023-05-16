"""fetrisa_toy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from main_store.views import (
    ItemViewSet,
    PatternViewSet,
    RegistrationView,
    JWTTokenObtainPairView,
    UserList,
    UserDetailView,
    AllItemViewSet,
    bucket_create_view,
    BuketList,
    like_create_view,
    LikeList,
    CheckBucketItemAPI,
    UpdateBucketItemAPI,
    CheckLikeItemAPI,
    RemoveLikeAPI,
    RemoveBuketAPI,
    create_order,
    UserUpdateAPIView,
    upload_file,
    ResetPasswordView,
    reset_password_api,
)

router = SimpleRouter()
router.register(r"items", ItemViewSet, basename="items")
router.register(r"pattern", PatternViewSet, basename="pattern")

urlpatterns = (
    [
        path("reset-password-api/<str:token>", reset_password_api, name="reset_password_api"),
        path("reset-password/", ResetPasswordView.as_view(), name="reset_password"),
        path("upload/", upload_file, name="upload_file"),
        path("users/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update"),
        path("auth/register/", RegistrationView.as_view(), name="register"),
        path("auth/token/", JWTTokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("auth/token/refresh/", JWTTokenObtainPairView.as_view(), name="token_refresh"),
        path("users/", UserList.as_view(), name="user_list"),
        path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
        path("items/<int:id>/", AllItemViewSet.as_view(), name="item-detail"),
        path("bucket/create/", bucket_create_view, name="bucket_create"),
        path("bucket/user/<int:user_id>/", BuketList.as_view(), name="buket-user-list"),
        path("like/create/", like_create_view, name="like_create"),
        path("like/user/<int:user_id>/", LikeList.as_view(), name="like-user-list"),
        path("check-bucket-item/", CheckBucketItemAPI.as_view(), name="check_bucket_item"),
        path("check-like-item/", CheckLikeItemAPI.as_view(), name="check_like_item"),
        path("update-bucket-item/", UpdateBucketItemAPI.as_view(), name="update-bucket-item"),
        path("remove-like-item/", RemoveLikeAPI.as_view(), name="remove-like-item"),
        path("remove-bucket-item/", RemoveBuketAPI.as_view(), name="remove-bucket-item"),
        path("create-order/", create_order, name="create-order"),
    ]
    + router.urls
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
