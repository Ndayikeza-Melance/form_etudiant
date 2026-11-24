
import os

from django.core.exceptions import ValidationError


ALLOWED_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
]

MAX_IMAGE_SIZE_MB = 5


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()

    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            "Extension d'image non autorisée."
        )


def validate_file_size(value):
    limit = MAX_IMAGE_SIZE_MB * 1024 * 1024

    if value.size > limit:
        raise ValidationError(
            "La taille maximale autorisée est de 5 Mo."
        )
