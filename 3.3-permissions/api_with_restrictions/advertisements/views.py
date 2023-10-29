from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet
# from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter, FavoriteFilter
from advertisements.models import Advertisement, Favorite
from advertisements.permission import IsOwnerOrReadOnly, IsNotOwner
from advertisements.serializers import AdvertisementSerializer, FavoriteSerializer


class CustomSearchFilter:
    pass


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []


class FavoriteViewSet(ModelViewSet):
    """ViewSet для избранного."""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, IsNotOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FavoriteFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'destroy']:
            return [IsAuthenticated(), IsNotOwner()]
        return []