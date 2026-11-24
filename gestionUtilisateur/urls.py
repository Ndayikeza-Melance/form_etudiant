from django.urls import path, include
urlpatterns = [path("personnes/",include("gestionUtilisateur.modules.personnes.urls")),]
