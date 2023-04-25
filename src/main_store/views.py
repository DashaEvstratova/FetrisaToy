from main_store.serializers import ItemSerializer, PicturesSerializer
from main_store.models import Items, Pictures
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q

class ItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        return ItemSerializer
    def get_queryset(self):
        return (
            Items.objects.filter(category='Игрушки'))

class PicturesSet(ModelViewSet):
    def get_serializer_class(self):
        return PicturesSerializer
    def get_queryset(self):
        pictures = []
        items = Items.objects.filter(
            Q(pictures__isnull=False, category='Игрушки')).distinct()
        for item in items:
            pictures.append(item.pictures.all())
        print(pictures)
        return pictures