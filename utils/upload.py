
import os
import uuid

from django.utils import timezone


def upload_to_dated_path(instance, filename, subdir="uploads"):
    ext = os.path.splitext(filename)[1].lower()

    date_path = timezone.now().strftime("%d-%m-%Y")

    new_filename = f"{uuid.uuid4().hex}{ext}"

    return os.path.join(
        subdir,
        date_path,
        new_filename,
    )
