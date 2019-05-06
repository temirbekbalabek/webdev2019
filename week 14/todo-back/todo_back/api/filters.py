from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    # status = filters.NumberFilter(field_name='s', lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ('name',)
