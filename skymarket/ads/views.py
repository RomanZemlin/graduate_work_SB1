from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import AdFilter
from .models import Ad
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    # serializer_class = AdSerializer
    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update', 'destroy']:
            return AdDetailSerializer
        return AdSerializer

    # permission_classes = (AllowAny,)
    def get_permissions(self):
        permission_classes = (AllowAny,)
        if self.action == 'retrieve':
            permission_classes = (IsAuthenticated,)
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = (IsOwner | IsAdmin,)
        return [permission() for permission in permission_classes]

    # queryset = Ad.objects.all()
    def get_queryset(self):
        queryset = Ad.objects.select_related('author')
        if self.action == 'own_ads':
            queryset = queryset.filter(author=self.request.user)
        return queryset.all()

    @action(detail=False, methods=['GET'], url_path='me')
    def own_ads(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=user, ad=ad)

    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = (IsOwner | IsAdmin,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        return ad.comments.all()  # Comment.objects.filter(ad_id=ad_id)(ad=ad)
