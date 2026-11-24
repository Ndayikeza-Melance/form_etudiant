from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Personne
from .services import PersonneService


class PersonneSerializer(serializers.ModelSerializer):
    """
    Serializer principal pour la gestion des personnes.
    """
    mot_passe = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=False,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = Personne
        fields = [
            "id",
            "nom",
            "prenom",
            "telephone",
            "email",
            "date_naissance",
            "nationalite",
            "role",
            "type_personne",
            "mot_passe",
            "date_creation",
            "date_modification",
        ]

        read_only_fields = [
            "id",
            "date_creation",
            "date_modification",
        ]

    def validate(self, attrs):
        """
        Vérifier les données avant leur enregistrement.
        """
        if self.instance is None and not attrs.get("mot_passe"):
            raise serializers.ValidationError({
                "mot_passe": "Le mot de passe est obligatoire."
            })
        return attrs
    def create(self, validated_data):
        """
        Créer une personne via le service métier.
        """
        return PersonneService.creer_personne(validated_data)
    def update(self, instance, validated_data):
        """
        Modifier une personne via le service métier.
        """
        personne = PersonneService.modifier_personne(instance.id,validated_data)
        if personne is None:
            raise serializers.ValidationError("Impossible de retrouver cette personne.")
        return personne
