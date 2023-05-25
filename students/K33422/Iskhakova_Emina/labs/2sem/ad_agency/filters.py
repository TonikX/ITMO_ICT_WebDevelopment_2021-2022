from django_filters import rest_framework as filters
from .models import *


class ChosenMaterialsRangeFilter(filters.FilterSet):
    amount = filters.RangeFilter()
    ordering = filters.OrderingFilter(fields=(('amount'),))

    class Meta:
        model = ChosenMaterials
        fields = ['amount']
