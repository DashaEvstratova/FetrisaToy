from rest_framework import serializers

from main_store.models import Items, Pictures, User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = (
            "name",
            "number",
            "size",
            "price",
            "description",
            "category",
        )


class PicturesSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Pictures
        fields = (
            "picture",
            "item",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "surname",
            "patronymic",
            "avatar",
            "city",
            "street",
            "house",
            "corps",
            "apartment",
            "phone_number",
            "date_of_birth",
        )
