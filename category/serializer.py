from rest_framework import serializers
from .models import Category, Product, ImageProduct


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['__all__']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['image',]


class ProductSerializer(serializers.ModelSerializer):
    product = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'