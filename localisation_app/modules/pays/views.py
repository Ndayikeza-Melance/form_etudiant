
from rest_framework.permissions import IsAuthenticated

from rest_flex_fields.views import FlexFieldsModelViewSet

from .models import Equipement
from .serializers import (
    EquipementReadSerializer,
    EquipementWriteSerializer,
)
from .filters import EquipementFilter


class EquipementViewSet(FlexFieldsModelViewSet):

    queryset = (
        Equipement.objects
        .select_related(
            "type_equipement",
            "statut",
            "entrepot",
        )
        .order_by("-date_creation")
    )

    serializer_class = EquipementReadSerializer

    serializer_class_read = EquipementReadSerializer
    serializer_class_write = EquipementWriteSerializer

    filterset_class = EquipementFilter

    permit_list_expands = [
        "type_equipement",
        "statut",
        "entrepot",
    ]

    permission_classes = [
        IsAuthenticated,
    ]
