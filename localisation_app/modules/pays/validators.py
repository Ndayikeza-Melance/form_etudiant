
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
            f"Extension non autorisée : {ext}. "
            f"Extensions autorisées : "
            f"{', '.join(ALLOWED_IMAGE_EXTENSIONS)}"
        )


def validate_file_size(value, max_size_mb=MAX_IMAGE_SIZE_MB):
    limit = max_size_mb * 1024 * 1024

    if value.size > limit:
        raise ValidationError(
            f"Le fichier dépasse {max_size_mb} Mo."
        )
