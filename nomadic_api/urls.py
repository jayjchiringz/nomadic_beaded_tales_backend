from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListCreate
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore

urlpatterns = [
]


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
