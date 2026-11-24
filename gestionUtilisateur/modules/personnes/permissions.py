from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPersonneAdmin(BasePermission):
    """
    Réserve toutes les opérations aux administrateurs.
    """
    message = "Seuls les administrateurs peuvent effectuer cette opération."
    def has_permission(self, request, view):
        utilisateur = request.user
        return bool(
            utilisateur
            and utilisateur.is_authenticated
            and (
                utilisateur.is_staff
                or utilisateur.is_superuser
            )
        )

class IsAdminOrReadOnly(BasePermission):
    """
    Lecture réservée aux utilisateurs authentifiés.
    Modification réservée aux administrateurs.
    """
    message = "Vous n'avez pas les autorisations nécessaires."
    def has_permission(self, request, view):
        utilisateur = request.user
        if not utilisateur or not utilisateur.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return (
            utilisateur.is_staff
            or utilisateur.is_superuser
        )
class IsAuthenticatedOrCreate(BasePermission):
    """
    Autorise l'inscription publique.
    Les autres opérations nécessitent une authentification.
    """
    def has_permission(self, request, view):
        utilisateur = request.user
        if request.method == "POST":
            return True
        return bool(utilisateur and utilisateur.is_authenticated)

class IsPersonneOwner(BasePermission):
    """
    Autorise l'accès uniquement au propriétaire.
    Nécessite une relation entre le modèle utilisateur
    Django et le modèle Personne.
    """
    message = "Vous ne pouvez accéder qu'à vos propres données."
    def has_object_permission(self, request, view, obj):
        utilisateur = request.user
        if not utilisateur or not utilisateur.is_authenticated:
            return False
        # À adapter lorsque la relation sera créée.
        return (
            hasattr(obj, "utilisateur_id")
            and obj.utilisateur_id == utilisateur.pk
        )
