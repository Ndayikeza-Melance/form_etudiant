
import re
from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def valider_nom(value):
    """Valider un nom ou un prénom."""

    if not value or not value.strip():
        raise ValidationError("Ce champ est obligatoire.")

    value = value.strip()

    if len(value) < 2:
        raise ValidationError(
            "Le nom doit contenir au moins 2 caractères."
        )

    if len(value) > 150:
        raise ValidationError(
            "Le nom ne doit pas dépasser 150 caractères."
        )

    if not re.fullmatch(r"[^\W\d_]+(?:[ '\u2019-][^\W\d_]+)*", value, re.UNICODE):
        raise ValidationError(
            "Le nom contient des caractères invalides."
        )

    return value


def valider_telephone(value):
    """Valider un numéro de téléphone."""

    if not value:
        raise ValidationError(
            "Le numéro de téléphone est obligatoire."
        )

    telephone = re.sub(r"[\s().-]", "", value)

    if not re.fullmatch(r"\+?[0-9]{8,15}", telephone):
        raise ValidationError(
            "Le numéro de téléphone est invalide."
        )

    return telephone


def valider_email(value):
    """Valider une adresse email."""

    if not value or not value.strip():
        raise ValidationError(
            "L'adresse email est obligatoire."
        )

    value = value.strip().lower()

    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError(
            "L'adresse email est invalide."
        )

    return value


def valider_date_naissance(value):
    """Vérifier la date de naissance."""

    if not value:
        raise ValidationError(
            "La date de naissance est obligatoire."
        )

    if value >= date.today():
        raise ValidationError(
            "La date de naissance doit être antérieure à aujourd'hui."
        )

    return value


def valider_nationalite(value):
    """Valider la nationalité."""

    if not value or not value.strip():
        raise ValidationError(
            "La nationalité est obligatoire."
        )

    value = value.strip()

    if len(value) < 2 or len(value) > 100:
        raise ValidationError(
            "La nationalité doit contenir entre 2 et 100 caractères."
        )

    return value


def valider_role(value):
    """Valider le rôle."""

    roles_autorises = [
        "admin",
        "utilisateur",
        "gestionnaire",
    ]

    if not value or not value.strip():
        raise ValidationError(
            "Le rôle est obligatoire."
        )

    value = value.strip().lower()

    if value not in roles_autorises:
        raise ValidationError(
            "Ce rôle n'est pas autorisé."
        )

    return value


def valider_type_personne(value):
    """Valider le type de personne."""

    if not value or not value.strip():
        raise ValidationError(
            "Le type de personne est obligatoire."
        )

    value = value.strip()

    if len(value) > 50:
        raise ValidationError(
            "Le type de personne ne doit pas dépasser 50 caractères."
        )

    return value
