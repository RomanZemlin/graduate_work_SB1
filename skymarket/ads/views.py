from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, permissions, generics

from .models import Ad, Comment
from .serializers import (
    AdSerializer,
    CommentSerializer,
    AdDetailSerializer,
    AdCreateSerializer,
    CommentCreateSerializer,
)

from .filters import AdFilter

from .permissions import IsOwnerOrStaff


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdMyListAPIView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        elif self.action == "retrieve":
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if (
            self.action == "create"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            return AdCreateSerializer
        elif self.action == "retrieve":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Comment.objects.filter(ad_id=self.kwargs["ad_pk"])
        return queryset

    def get_serializer_class(self):
        if (
            self.action == "create"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs["ad_pk"])
