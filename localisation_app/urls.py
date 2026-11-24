
from django.urls import path
from rest_framework.routers import DefaultRouter

from localisation_app.modules.communes.views import (
    CommuneViewSet,
    exclude_polygons,
)
from localisation_app.modules.provinces.views import ProvinceViewSet

router = DefaultRouter()

router.register(
    "communes",
    CommuneViewSet,
    basename="commune",
)

router.register(
    "provinces",
    ProvinceViewSet,
    basename="province",
)

urlpatterns = [
    path(
        "communes/exclude-polygons/",
        exclude_polygons,
        name="exclude_polygons",
    ),
]

urlpatterns += router.urls
