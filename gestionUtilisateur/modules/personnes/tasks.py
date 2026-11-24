
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

from .models import Personne


@shared_task
def compter_personnes():
    """Compter le nombre total de personnes."""

    return Personne.objects.count()


@shared_task
def rechercher_personne_par_email(email):
    """Rechercher une personne par email."""

    if not email:
        return False

    return Personne.objects.filter(
        email__iexact=email.strip()
    ).exists()


@shared_task
def supprimer_personnes_inactives():
    """
    Tâche en attente de définition du critère d'inactivité.
    """

    return {
        "success": False,
        "message": "Aucun critère d'inactivité défini."
    }


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def envoyer_email_personne(self, personne_id, sujet, message):
    """Envoyer un email à une personne."""

    personne = Personne.objects.filter(
        id=personne_id
    ).first()

    if not personne:
        return {
            "success": False,
            "message": "Personne introuvable."
        }

    resultat = send_mail(
        subject=sujet,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[personne.email],
        fail_silently=False,
    )

    if resultat == 1:
        return {
            "success": True,
            "message": "Email envoyé avec succès."
        }

    raise Exception("L'envoi de l'email a échoué.")


@shared_task
def statistiques_personnes():
    """Générer des statistiques."""

    return {
        "total_personnes": Personne.objects.count(),
        "date_generation": timezone.now().isoformat(),
    }


@shared_task
def verifier_doublons_personnes():
    """Identifier les emails et téléphones dupliqués."""

    emails = list(
        Personne.objects.values("email")
        .annotate(total=Count("id"))
        .filter(total__gt=1)
    )

    telephones = list(
        Personne.objects.values("telephone")
        .annotate(total=Count("id"))
        .filter(total__gt=1)
    )

    return {
        "emails_dupliques": emails,
        "telephones_dupliques": telephones,
    }
