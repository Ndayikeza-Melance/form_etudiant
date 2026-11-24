
from django.urls import include, path

urlpatterns = [
    path("", include("authentification.urls")),
    path("",include("gestionUtilisateur.urls"),),
    path("localisation/",include("localisation_app.urls"),),
    path("equipements/",include("equipements_app.modules.equipements.urls"),),
]
