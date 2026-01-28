from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer

from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import AllowAny

class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]   # ✅ TEMP FIX



from rest_framework.generics import RetrieveUpdateDestroyAPIView
class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]

