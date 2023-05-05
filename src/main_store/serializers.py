from rest_framework import serializers

from main_store.models import Items, Pictures, User, Buket, Likes



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
            "id"
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


class BucketCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    item = serializers.IntegerField()

    def create(self, validated_data):
        user_id = validated_data["user"]
        item_id = validated_data["item"]
        user = User.objects.get(id=user_id)
        item = Items.objects.get(id=item_id)
        bucket = Buket.objects.create(user=user, item=item)
        return bucket

class LikeCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    item = serializers.IntegerField()

    def create(self, validated_data):
        user_id = validated_data["user"]
        item_id = validated_data["item"]
        user = User.objects.get(id=user_id)
        item = Items.objects.get(id=item_id)
        bucket = Likes.objects.create(user=user, item=item)
        return bucket

class PictureBuketSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(max_length=255)
    item_id = serializers.IntegerField()

    class Meta:
        model = Pictures
        fields = ["picture", "item_id"]

class ItemBuketSerializer(serializers.ModelSerializer):
    pictures = PictureBuketSerializer(many=True)

    class Meta:
        model = Items
        fields = ["id", "name", "description", "price", "pictures"]

class BuketSerializer(serializers.ModelSerializer):
    item = ItemBuketSerializer()

    class Meta:
        model = Buket
        fields = ["id", "user", "item"]

    def get_picture(self, obj):
        return obj.item.pictures.first().picture

class LikeSerializer(serializers.ModelSerializer):
    item = ItemBuketSerializer()

    class Meta:
        model = Buket
        fields = ["id", "user", "item"]

    def get_picture(self, obj):
        return obj.item.pictures.first().picture