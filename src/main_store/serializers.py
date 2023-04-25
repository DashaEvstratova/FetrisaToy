from rest_framework import serializers

from main_store.models import Items, Pictures


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = (
            "picture",
            "item",
        )

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
