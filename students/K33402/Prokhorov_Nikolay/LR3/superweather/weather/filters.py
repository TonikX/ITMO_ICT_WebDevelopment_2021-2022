from django_filters.rest_framework import FilterSet, NumberFilter


class DailyFilterSet(FilterSet):
    weekday = NumberFilter(field_name='weekday')
