from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


def accueil(request):
    """Page d'accueil de l'API."""
    return JsonResponse({
        "message": "Bienvenue dans l'API de gestion des personnes",
        "status": "success",
        "api": "/api/personnes/",
        "admin": "/admin/",
        "documentation": "/api/documentation/"
    })

urlpatterns = [
    path("", accueil, name="accueil"),
    path("admin/", admin.site.urls),
    path("api/",include("gestionUtilisateur.urls")),
]

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
