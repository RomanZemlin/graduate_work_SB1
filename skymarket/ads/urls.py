from django.urls import path
from rest_framework_nested import routers
from .apps import SalesConfig
from .views import AdMe, AdViewSet, CommentViewSet

app_name = SalesConfig.name

urlpatterns = [
    path('ads/me/', AdMe.as_view(), name='list_me'),
]

router = routers.SimpleRouter()
router.register('ads', AdViewSet)
comments_router = routers.NestedSimpleRouter(router, r'ads', lookup='ad')
comments_router.register(r'comments', CommentViewSet, basename='ad-comments')

urlpatterns += router.urls
urlpatterns += comments_router.urls
