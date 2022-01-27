from django.db.models import Q
from django_filters.rest_framework import FilterSet, NumberFilter, CharFilter


def city_name_filter(queryset, name, value):
    return queryset.filter(Q(name__icontains=value) | Q(name_ru__icontains=value))


class CityFilterSet(FilterSet):
    q = CharFilter(method=city_name_filter)


class DailyFilterSet(FilterSet):
    weekday = NumberFilter(field_name='weekday')
