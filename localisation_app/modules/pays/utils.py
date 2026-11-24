
import os
import uuid

from datetime import date


def upload_to_dated_path(instance, filename, subdir="uploads"):
    """
    Génère un chemin standardisé :

    subdir/jj-mm-aaaa/uuid.extension
    """

    ext = os.path.splitext(filename)[1].lower().lstrip(".")

    date_path = date.today().strftime("%d-%m-%Y")

    new_filename = f"{uuid.uuid4().hex}.{ext}"

    return os.path.join(
        subdir,
        date_path,
        new_filename,
    )
