import django_filters
from django.utils import timezone
from .models import Personne
class PersonneFilter(django_filters.FilterSet):
    """
    Filtres avancés pour le modèle Personne.
    """
    nom = django_filters.CharFilter(field_name="nom",lookup_expr="icontains")
    prenom = django_filters.CharFilter(field_name="prenom",lookup_expr="icontains")
    telephone = django_filters.CharFilter(field_name="telephone",lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email",lookup_expr="icontains")
    nationalite = django_filters.CharFilter(field_name="nationalite",lookup_expr="icontains")
    role = django_filters.CharFilter(field_name="role",lookup_expr="iexact")
    type_personne = django_filters.CharFilter(field_name="type_personne",lookup_expr="iexact")
    date_naissance = django_filters.DateFilter(field_name="date_naissance")
    date_naissance_min = django_filters.DateFilter(field_name="date_naissance",lookup_expr="gte")
    date_naissance_max = django_filters.DateFilter(field_name="date_naissance",lookup_expr="lte")
    annee_naissance = django_filters.NumberFilter(field_name="date_naissance__year")
    def filter_date_future(self, queryset, name, value):
        """
        Empêcher les recherches avec une date future.
        """
        if value and value > timezone.localdate():
            return queryset.none()
        return queryset

    class Meta:
        model = Personne
        fields = [
            "nom",
            "prenom",
            "telephone",
            "email",
            "nationalite",
            "role",
            "type_personne",
            "date_naissance",
        ]
