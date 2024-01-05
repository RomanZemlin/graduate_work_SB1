from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import pagination, viewsets, generics, status
from rest_framework.permissions import IsAuthenticated

from .models import Ad, Comment
from .permissions import CustomPermission, UserPermission
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = "page_size"


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']
    permission_classes = [CustomPermission, UserPermission]

    def get_serializer_class(self):
        """При детальном просмотре объявления оброщение к сериализатору
        AdDetailSerializer """
        if self.action == 'retrieve':
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        """При создании объявлений его владелец, авторизованный пользователь """
        new_ad = serializer.save(author=self.request.user)
        new_ad.author = self.request.user
        new_ad.save()


class AdMe(generics.ListAPIView):
    """Просмотр списка объявлений пользователя"""
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user:
            queryset = queryset.filter(author=self.request.user.pk)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    """Просмотр комментариев к объявлениям"""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def get_queryset(self):
        return Comment.objects.filter(ad__id=self.kwargs['ad_pk'])

    def create(self, request, ad_pk=None):
        ad = Ad.objects.get(pk=ad_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ad=ad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
