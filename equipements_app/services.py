
from django.db import transaction

from .models import Equipement


@transaction.atomic
def creer_equipement(data):
    """
    Crée un équipement dans une transaction.
    """
    equipement = Equipement.objects.create(**data)

    return equipement


@transaction.atomic
def modifier_equipement(equipement, data):
    """
    Modifie un équipement.
    """
    for field, value in data.items():
        setattr(equipement, field, value)

    equipement.save()

    return equipement


@transaction.atomic
def supprimer_equipement(equipement):
    """
    Supprime un équipement.
    """
    equipement.delete()
