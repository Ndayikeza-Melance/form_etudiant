
import django_filters

from .models import Equipement


class EquipementFilter(django_filters.FilterSet):
    """
    Filtres disponibles pour les équipements :

    - device_id
    - numero_serie
    - type_equipement
    - statut
    - entrepot
    - date_creation
    - date_creation_gte
    - date_creation_lte
    """

    # Filtrage par date exacte
    date_creation = django_filters.DateFilter(
        field_name="date_creation",
        lookup_expr="date",
    )

    # Filtrage à partir d'une date
    date_creation_gte = django_filters.DateFilter(
        field_name="date_creation",
        lookup_expr="date__gte",
    )

    # Filtrage jusqu'à une date
    date_creation_lte = django_filters.DateFilter(
        field_name="date_creation",
        lookup_expr="date__lte",
    )

    # Recherche partielle sur les identifiants
    device_id = django_filters.CharFilter(
        field_name="device_id",
        lookup_expr="icontains",
    )

    numero_serie = django_filters.CharFilter(
        field_name="numero_serie",
        lookup_expr="icontains",
    )

    class Meta:
        model = Equipement

        fields = [
            "type_equipement",
            "statut",
            "entrepot",
        ]
