
from django.db import models

from localisation_app.utils.files import upload_to_dated_path
from localisation_app.utils.validators import (
    validate_image_extension,
    validate_file_size,
)


def equipement_photo_upload_to(instance, filename):
    return upload_to_dated_path(
        instance,
        filename,
        subdir="equipements/photos",
    )


class Equipement(models.Model):

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

    class Meta:
        db_table = "equipements"

    def __str__(self):
        return f"Equipement {self.pk}"
