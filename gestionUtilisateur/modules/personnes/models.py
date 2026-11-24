
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone


class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    date_naissance = models.DateField()
    nationalite = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    type_personne = models.CharField(max_length=50)
    mot_passe = models.CharField(max_length=128,editable=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personnes"
        ordering = ["nom", "prenom"]
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"

    def clean(self):
        super().clean()
        self.nom = self.nom.strip() if self.nom else self.nom
        self.prenom = self.prenom.strip() if self.prenom else self.prenom

        if self.email:
            self.email = self.email.strip().lower()
            validate_email(self.email)

        if self.telephone:
            self.telephone = self.telephone.strip()

        if self.date_naissance:
            if self.date_naissance >= timezone.localdate():
                raise ValidationError({
                    "date_naissance":
                    "La date de naissance doit être antérieure à aujourd'hui."
                })

    def set_password(self, raw_password):
        if not raw_password:
            raise ValueError("Le mot de passe ne peut pas être vide.")
        self.mot_passe = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(
            raw_password,
            self.mot_passe
        )
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nom} {self.prenom}"
