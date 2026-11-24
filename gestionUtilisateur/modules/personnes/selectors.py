from django.db.models import Q
from .models import Personne
from .utils import normaliser_email, normaliser_telephone


class PersonneSelector:
    """
    Sélecteurs pour récupérer et consulter les personnes.
    """
    @staticmethod
    def obtenir_toutes():
        """Récupérer toutes les personnes."""
        return Personne.objects.all().order_by(
            "nom",
            "prenom"
        )

    @staticmethod
    def obtenir_par_id(personne_id):
        """Rechercher une personne par identifiant."""
        return Personne.objects.filter(
            id=personne_id
        ).first()

    @staticmethod
    def obtenir_par_email(email):
        """Rechercher une personne par email."""
        if not email:
            return None
        email = normaliser_email(email)
        return Personne.objects.filter(
            email__iexact=email
        ).first()

    @staticmethod
    def obtenir_par_telephone(telephone):
        """Rechercher une personne par téléphone."""

        if not telephone:
            return None

        telephone = normaliser_telephone(telephone)

        return Personne.objects.filter(
            telephone=telephone
        ).first()

    @staticmethod
    def obtenir_par_nom(nom):
        """Rechercher les personnes par nom."""
        if not nom or not nom.strip():
            return Personne.objects.none()
        return Personne.objects.filter(
            nom__icontains=nom.strip()
        ).order_by("nom", "prenom")

    @staticmethod
    def obtenir_par_role(role):
        """Récupérer les personnes selon leur rôle."""
        if not role:
            return Personne.objects.none()
        return Personne.objects.filter(
            role__iexact=role.strip()
        ).order_by("nom", "prenom")

    @staticmethod
    def obtenir_par_type(type_personne):
        """Récupérer les personnes selon leur type."""
        if not type_personne:
            return Personne.objects.none()
        return Personne.objects.filter(
            type_personne__iexact=type_personne.strip()
        ).order_by("nom", "prenom")

    @staticmethod
    def rechercher(mot_cle):
        """Recherche générale dans plusieurs champs."""
        if not mot_cle or not mot_cle.strip():
            return Personne.objects.none()
        mot_cle = mot_cle.strip()
        return Personne.objects.filter(
            Q(nom__icontains=mot_cle)
            | Q(prenom__icontains=mot_cle)
            | Q(email__icontains=mot_cle)
            | Q(telephone__icontains=mot_cle)
            | Q(nationalite__icontains=mot_cle)
            | Q(role__icontains=mot_cle)
            | Q(type_personne__icontains=mot_cle)
        ).order_by("nom", "prenom")

    @staticmethod
    def compter_personnes():
        """Compter le nombre total de personnes."""
        return Personne.objects.count()

    @staticmethod
    def compter_par_role(role):
        """Compter les personnes selon leur rôle."""
        if not role:
            return 0
        return Personne.objects.filter(
            role__iexact=role.strip()
        ).count()

    @staticmethod
    def verifier_email_existant(email, exclure_id=None):
        """Vérifier si un email est déjà utilisé."""
        if not email:
            return False
        email = normaliser_email(email)
        queryset = Personne.objects.filter(
            email__iexact=email
        )
        if exclure_id is not None:
            queryset = queryset.exclude(id=exclure_id)
        return queryset.exists()

    @staticmethod
    def verifier_telephone_existant(telephone, exclure_id=None):
        """Vérifier si un téléphone est déjà utilisé."""
        if not telephone:
            return False
        telephone = normaliser_telephone(telephone)
        queryset = Personne.objects.filter(
            telephone=telephone
        )
        if exclure_id is not None:
            queryset = queryset.exclude(id=exclure_id)
        return queryset.exists()
