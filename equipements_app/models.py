
from utils.upload import upload_to_dated_path
from utils.validators import (
    validate_image_extension,
    validate_file_size,
)

from equipements_app.modules.equipements.models import (
    TypeEquipement,
    StatutEquipement,
    Equipement,
)




class TypeEquipement(models.Model):
    nom = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = "types_equipements"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class StatutEquipement(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "statuts_equipements"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Equipement(models.Model):
    type_equipement = models.ForeignKey(
        TypeEquipement,
        on_delete=models.PROTECT,
        related_name="equipements",
    )

    device_id = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True,
    )

    numero_serie = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )

    statut = models.ForeignKey(
        StatutEquipement,
        on_delete=models.PROTECT,
        related_name="equipements",
    )

    entrepot = models.ForeignKey(
        "localisation_app.Entrepot",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="equipements",
    )

    photo = models.ImageField(
        upload_to="equipements/photos/",
        null=True,
        blank=True,
        max_length=300,
    )

    date_fin_garantie = models.DateField(
        null=True,
        blank=True,
    )

    date_creation = models.DateTimeField(
        auto_now_add=True,
    )

    date_modification = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "equipements"
        ordering = ["-date_creation"]
        indexes = [
            models.Index(fields=["date_creation"]),
            models.Index(fields=["numero_serie"]),
        ]

    def __str__(self):
        return (
            f"{self.numero_serie or 'Sans numéro'} - "
            f"{self.device_id or 'Sans device ID'}"
        )


def equipement_photo_upload_to(instance, filename):
    return upload_to_dated_path(
        instance,
        filename,
        subdir="equipements/photos",
    )


# Dans le modèle Equipement :
photo = models.ImageField(
    upload_to=equipement_photo_upload_to,
    validators=[
        validate_image_extension,
        validate_file_size,
    ],
    null=True,
    blank=True,
    max_length=300,
)
