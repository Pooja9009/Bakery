import django_filters
from .models import Cake, Category

class CakeFilters(django_filters.FilterSet):
    cake_contains = django_filters.CharFilter(field_name='cake_name', lookup_expr='icontains')
    class Meta:
        model = Cake
        fields = []

class CategoryFilters(django_filters.FilterSet):
    cake_contains = django_filters.CharFilter(field_name='category_name', lookup_expr='icontains')
    class Meta:
        model = Category
        fields = []

