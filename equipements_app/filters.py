
import django_filters

from .models import Equipement


class EquipementFilter(django_filters.FilterSet):

    date_creation = django_filters.DateFilter(
        field_name="date_creation",
        lookup_expr="date",
    )

    date_creation_gte = django_filters.DateTimeFilter(
        field_name="date_creation",
        lookup_expr="gte",
    )

    date_creation_lte = django_filters.DateTimeFilter(
        field_name="date_creation",
        lookup_expr="lte",
    )

    numero_serie = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    class Meta:
        model = Equipement
        fields = [
            "device_id",
            "type_equipement",
            "statut",
            "numero_serie",
            "entrepot",
        ]
