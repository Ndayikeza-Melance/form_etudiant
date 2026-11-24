
import re
import secrets
import string

from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def nettoyer_texte(value):
    """Supprimer les espaces inutiles."""

    if not isinstance(value, str):
        return value

    return " ".join(value.strip().split())


def normaliser_email(email):
    """Normaliser une adresse email."""

    if not email:
        return ""

    return email.strip().lower()


def normaliser_telephone(telephone):
    """Normaliser un numéro de téléphone."""

    if not telephone:
        return ""

    return re.sub(
        r"[\s().-]",
        "",
        telephone.strip()
    )


def normaliser_nom(nom):
    """Normaliser un nom ou un prénom."""

    if not nom:
        return ""

    return nettoyer_texte(nom)


def generer_mot_passe(longueur=12):
    """Générer un mot de passe aléatoire sécurisé."""

    if not isinstance(longueur, int) or isinstance(longueur, bool):
        raise ValueError("La longueur doit être un entier.")

    if longueur < 8 or longueur > 128:
        raise ValueError(
            "La longueur doit être comprise entre 8 et 128 caractères."
        )

    caracteres = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()-_"
    )

    while True:

        mot_passe = "".join(
            secrets.choice(caracteres)
            for _ in range(longueur)
        )

        if (
            any(c.islower() for c in mot_passe)
            and any(c.isupper() for c in mot_passe)
            and any(c.isdigit() for c in mot_passe)
            and any(c in "!@#$%^&*()-_" for c in mot_passe)
        ):
            return mot_passe


def calculer_age(date_naissance):
    """Calculer l'âge d'une personne."""

    if not date_naissance:
        return None

    aujourd_hui = timezone.localdate()

    age = aujourd_hui.year - date_naissance.year

    if (
        (aujourd_hui.month, aujourd_hui.day)
        < (date_naissance.month, date_naissance.day)
    ):
        age -= 1

    return age


def formater_nom_complet(personne):
    """Retourner le nom complet."""

    return nettoyer_texte(
        f"{personne.nom} {personne.prenom}"
    )


def obtenir_date_actuelle():
    """Retourner la date et l'heure actuelles."""

    return timezone.now()


def masquer_telephone(telephone):
    """Masquer une partie du téléphone."""

    if not telephone:
        return telephone

    telephone = str(telephone)

    if len(telephone) < 4:
        return "*" * len(telephone)

    return "*" * (len(telephone) - 4) + telephone[-4:]


def masquer_email(email):
    """Masquer une partie d'une adresse email."""

    if not email:
        return email

    email = email.strip()

    try:
        validate_email(email)
    except ValidationError:
        return None

    nom, domaine = email.rsplit("@", 1)

    if len(nom) == 1:
        nom_masque = "*"
    elif len(nom) == 2:
        nom_masque = nom[0] + "*"
    else:
        nom_masque = nom[:2] + "*" * (len(nom) - 2)

    return f"{nom_masque}@{domaine}"
