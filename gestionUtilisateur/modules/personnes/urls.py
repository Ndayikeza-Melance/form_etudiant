from rest_framework.routers import DefaultRouter
from .views import PersonneViewSet

router = DefaultRouter()

router.register(
    r"",
    PersonneViewSet,
    basename="personne"
)

urlpatterns = router.urls