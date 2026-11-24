
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from django.utils import timezone

from .models import (
    Equipement,
    TypeEquipement,
    StatutEquipement,
)


class TypeEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEquipement
        fields = ["id", "nom"]


class StatutEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutEquipement
        fields = ["id", "nom"]


class EquipementReadSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Equipement
        fields = [
            "id",
            "type_equipement",
            "device_id",
            "numero_serie",
            "statut",
            "entrepot",
            "photo",
            "date_fin_garantie",
            "date_creation",
            "date_modification",
        ]

        expandable_fields = {
            "type_equipement": TypeEquipementSerializer,
            "statut": StatutEquipementSerializer,
        }


class EquipementWriteSerializer(
    FlexFieldsModelSerializer
):

    class Meta:
        model = Equipement
        fields = [
            "id",
            "type_equipement",
            "device_id",
            "numero_serie",
            "statut",
            "entrepot",
            "photo",
            "date_fin_garantie",
        ]

    def validate_numero_serie(self, value):
        queryset = Equipement.objects.filter(
            numero_serie=value
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if value and queryset.exists():
            raise serializers.ValidationError(
                "Ce numéro de série existe déjà."
            )

        return value

    def validate(self, attrs):
        date_fin = attrs.get(
            "date_fin_garantie",
            getattr(
                self.instance,
                "date_fin_garantie",
                None,
            ),
        )

        if date_fin and date_fin < timezone.localdate():
            raise serializers.ValidationError({
                "date_fin_garantie":
                    "La date de garantie ne peut pas être dans le passé."
            })

        return attrs
