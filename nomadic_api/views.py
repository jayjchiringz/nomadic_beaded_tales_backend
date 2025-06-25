from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Product
from .serializers import ProductSerializer

def echo_headers(request):
    return JsonResponse(dict(request.headers))

def api_health(request):
    return JsonResponse({"status": "ok", "headers": dict(request.headers)})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
