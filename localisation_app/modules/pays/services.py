from django.db import transaction
from .models import HistoriqueTransfert

@transaction.atomic
def transferer_equipement(equipement, entrepot_destination, utilisateur):
    """
    Transfère un équipement vers un autre entrepôt
    et enregistre son historique de transfert.
    """
    ancien_entrepot = equipement.entrepot_id

    equipement.entrepot = entrepot_destination
    equipement.save(update_fields=["entrepot"])

    HistoriqueTransfert.objects.create(
        equipement=equipement,
        entrepot_source_id=ancien_entrepot,
        entrepot_destination=entrepot_destination,
        effectue_par=utilisateur,
    )

    return equipement
