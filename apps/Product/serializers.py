from rest_framework import serializers
from .models import Category , Product , Favorite

# serializer -> category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


# serializer -> product
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'currency', 'location', 'category', 'image', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


# serializer -> favorite
class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ['user', 'product', 'added_at']
        read_only_fields = ['added_at']

