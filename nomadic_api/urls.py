from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # <-- handles all CRUD

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
