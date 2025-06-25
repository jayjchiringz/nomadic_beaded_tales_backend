from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, echo_headers, api_health
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('debug/headers/', echo_headers),
    path("api/health/", api_health),
]
