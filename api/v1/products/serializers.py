from rest_framework import serializers
from products.models import Product


from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        # ✅ Fixed default image
        return request.build_absolute_uri("/static/products/default.jpg")



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
