from main_store.serializers import ItemSerializer, PicturesSerializer
from main_store.models import Items, Pictures
from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch

class ItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        return PicturesSerializer
    def get_queryset(self):
        return Pictures.objects.all() \
            .prefetch_related(Prefetch("item", Items.objects.all().filter(category='Игрушки')))