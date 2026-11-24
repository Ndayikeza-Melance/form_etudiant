from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Personne


class PersonneService:
    """
    Services métier pour la gestion des personnes.
    """

    CHAMPS_MODIFIABLES = {
        "nom",
        "prenom",
        "telephone",
        "email",
        "date_naissance",
        "nationalite",
        "role",
        "type_personne",
    }

    CHAMPS_RECHERCHABLES = {
        "nom",
        "prenom",
        "email",
        "telephone",
        "nationalite",
        "role",
        "type_personne",
    }

    @staticmethod
    @transaction.atomic
    def creer_personne(data):
        """Créer une nouvelle personne."""

        data = data.copy()

        mot_passe = data.pop("mot_passe", None)

        if not mot_passe:
            raise ValidationError(
                "Le mot de passe est obligatoire."
            )

        personne = Personne(**data)

        personne.set_password(mot_passe)

        personne.save()

        return personne

    @staticmethod
    def obtenir_personne(personne_id):
        """Récupérer une personne par son identifiant."""

        return Personne.objects.filter(
            id=personne_id
        ).first()

    @staticmethod
    def lister_personnes():
        """Retourner toutes les personnes."""

        return Personne.objects.all().order_by(
            "nom",
            "prenom"
        )

    @staticmethod
    @transaction.atomic
    def modifier_personne(personne_id, data):
        """Modifier les informations d'une personne."""

        personne = PersonneService.obtenir_personne(
            personne_id
        )

        if personne is None:
            return None

        data = data.copy()

        mot_passe = data.pop("mot_passe", None)

        champs_interdits = (
            set(data.keys())
            - PersonneService.CHAMPS_MODIFIABLES
        )

        if champs_interdits:
            raise ValidationError(
                f"Champs non modifiables : {', '.join(champs_interdits)}"
            )

        for champ, valeur in data.items():
            setattr(personne, champ, valeur)

        if mot_passe is not None:
            personne.set_password(mot_passe)

        personne.save()

        return personne

    @staticmethod
    @transaction.atomic
    def supprimer_personne(personne_id):
        """Supprimer une personne."""

        personne = PersonneService.obtenir_personne(
            personne_id
        )

        if personne is None:
            return False

        personne.delete()

        return True

    @staticmethod
    def rechercher_personnes(**criteres):
        """Rechercher des personnes selon plusieurs critères."""

        queryset = Personne.objects.all()

        champs_autorises = (
            PersonneService.CHAMPS_RECHERCHABLES
        )

        for champ, valeur in criteres.items():

            if champ not in champs_autorises:
                raise ValidationError(
                    f"Critère de recherche non autorisé : {champ}"
                )

            if valeur is not None and valeur != "":
                queryset = queryset.filter(
                    **{f"{champ}__icontains": valeur}
                )

        return queryset.order_by(
            "nom",
            "prenom"
        )
