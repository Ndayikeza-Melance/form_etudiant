from django.contrib import admin
from django import forms
from .models import Personne


class PersonneAdminForm(forms.ModelForm):
    """
    Formulaire d'administration du modèle Personne.
    """
    nouveau_mot_passe = forms.CharField(
        label="Nouveau mot de passe",
        required=False,
        widget=forms.PasswordInput,
        help_text="Laisser vide pour conserver le mot de passe actuel."
    )

    class Meta:
        model = Personne
        exclude = ("mot_passe",)

    def save(self, commit=True):
        personne = super().save(commit=False)
        nouveau_mot_passe = self.cleaned_data.get("nouveau_mot_passe")
        if nouveau_mot_passe:
            from django.contrib.auth.password_validation import (validate_password)
            validate_password(nouveau_mot_passe)
            personne.set_password(nouveau_mot_passe)
        if commit:
            personne.save()
        return personne


@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration du modèle Personne.
    """
    form = PersonneAdminForm
    list_display = (
        "id",
        "nom",
        "prenom",
        "telephone",
        "email",
        "nationalite",
        "role",
        "type_personne",
        "date_creation",
    )
    list_display_links = (
        "id",
        "nom",
        "prenom",
    )
    list_filter = (
        "role",
        "type_personne",
        "nationalite",
        "date_creation",
    )
    search_fields = (
        "nom",
        "prenom",
        "telephone",
        "email",
        "nationalite",
    )
    ordering = (
        "nom",
        "prenom",
    )
    readonly_fields = (
        "date_creation",
        "date_modification",
    )
    list_per_page = 20
    fieldsets = (
        (
            "Informations personnelles",
            {
                "fields": (
                    "nom",
                    "prenom",
                    "date_naissance",
                    "nationalite",
                )
            },
        ),
        (
            "Coordonnées",
            {
                "fields": (
                    "telephone",
                    "email",
                )
            },
        ),
        (
            "Informations professionnelles",
            {
                "fields": (
                    "role",
                    "type_personne",
                )
            },
        ),
        (
            "Sécurité",
            {
                "fields": (
                    "nouveau_mot_passe",
                )
            },
        ),
        (
            "Informations système",
            {
                "fields": (
                    "date_creation",
                    "date_modification",
                )
            },
        ),
    )

    def has_delete_permission(self, request, obj=None):
        """Réserver la suppression aux superutilisateurs."""

        return request.user.is_superuser
