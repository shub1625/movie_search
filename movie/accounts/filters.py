import django_filters
from accounts.models import *




class MovieFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(field_name="title",lookup_expr="icontains")
    # year_gte = django_filters.NumberFilter(field_name="year",lookup_expr="gte")
    class Meta:
        model = Movie
        fields = {
            'title':['icontains'],
            'year':['iexact',],
            'rating':['exact'],
            'language':['iexact']
        }
        exclude = ['username','movie_pic']