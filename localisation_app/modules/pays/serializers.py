
from django.utils import timezone
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .models import Equipement


class EquipementWriteSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Equipement

        fields = [
            "id",
            "type_equipement",
            "statut",
            "entrepot",
            "device_id",
            "numero_serie",
            "photo",
            "date_fin_garantie",
        ]

    # Validation du numéro de série
    def validate_numero_serie(self, value):

        queryset = Equipement.objects.filter(
            numero_serie=value
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Ce numéro de série existe déjà."
            )

        return value

    # Validation générale
    def validate(self, attrs):

        date_fin = attrs.get(
            "date_fin_garantie",
            getattr(self.instance, "date_fin_garantie", None),
        )

        if date_fin and date_fin < timezone.localdate():
            raise serializers.ValidationError({
                "date_fin_garantie": (
                    "La date de fin de garantie ne peut pas être dans le passé."
                )
            })

        return attrs
