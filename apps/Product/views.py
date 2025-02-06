import django_filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# view -> category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# view -> product
class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label="Название продукта")
    category = django_filters.NumberFilter(field_name="category__id", label="Категория")
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Минимальная цена")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte', label="Максимальная цена")
    location = django_filters.CharFilter(lookup_expr='icontains', label="Местоположение")

    class Meta:
        model = Product
        fields = ['title', 'category', 'price_min', 'price_max', 'location']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['title', 'description', 'category__name']
    ordering_fields = ['created_at', 'price']
    filterset_fields = ['category', 'currency', 'location']

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


# view -> Favorite
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

