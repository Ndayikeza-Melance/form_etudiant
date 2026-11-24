
"""
Constantes du module personnes.
"""

# Longueurs maximales

MAX_NOM_LENGTH = 100
MAX_PRENOM_LENGTH = 150
MAX_TELEPHONE_LENGTH = 20
MAX_EMAIL_LENGTH = 254
MAX_NATIONALITE_LENGTH = 100
MAX_ROLE_LENGTH = 50
MAX_TYPE_PERSONNE_LENGTH = 50
MAX_PASSWORD_LENGTH = 128


# Rôles disponibles

ROLE_ADMIN = "ADMIN"
ROLE_UTILISATEUR = "UTILISATEUR"
ROLE_GESTIONNAIRE = "GESTIONNAIRE"
ROLE_MEMBRE = "MEMBRE"

ROLES_DISPONIBLES = (
    ROLE_ADMIN,
    ROLE_UTILISATEUR,
    ROLE_GESTIONNAIRE,
    ROLE_MEMBRE,
)

# Types de personnes
TYPE_PERSONNE_PHYSIQUE = "PHYSIQUE"
TYPE_PERSONNE_MORALE = "MORALE"
TYPES_PERSONNES_DISPONIBLES = (
    TYPE_PERSONNE_PHYSIQUE,
    TYPE_PERSONNE_MORALE,
)

# Messges de succès
MESSAGE_PERSONNE_CREEE = ("Personne créée avec succès.")
MESSAGE_PERSONNE_MODIFIEE = ("Personne modifiée avec succès.")
MESSAGE_PERSONNE_SUPPRIMEE = ("Personne supprimée avec succès.")
MESSAGE_PERSONNE_TROUVEE = ("Personne récupérée avec succès.")

# Messages d'erreur
ERREUR_PERSONNE_INTROUVABLE = ("Personne introuvable.")
ERREUR_EMAIL_EXISTANT = ("Cette adresse email est déjà utilisée.")
ERREUR_TELEPHONE_EXISTANT = ("Ce numéro de téléphone est déjà utilisé.")
ERREUR_DONNEES_INVALIDES = ("Les données fournies sont invalides.")
ERREUR_ACCES_REFUSE = ("Vous n'avez pas l'autorisation d'effectuer cette opération.")
# Pagination
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100
# Formats de données
FORMAT_DATE = "%Y-%m-%d"
FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
