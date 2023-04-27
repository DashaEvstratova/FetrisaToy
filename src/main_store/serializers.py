from rest_framework import serializers

from main_store.models import Items, Pictures


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