import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date",lookup_expr='gte')
    #end_date = DateFilter(field_name="date", lookup_expr='lte')
    nome = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields ='__all__'
        exclude = ['description', 'img','price','tags','name']
