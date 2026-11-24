
from rest_framework import viewsets, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Personne
from .serializers import PersonneSerializer
from .filters import PersonneFilter
from .permissions import IsPersonneAdmin


class PersonneViewSet(viewsets.ModelViewSet):

    """
    ViewSet pour gérer les opérations CRUD des personnes.
    """

    queryset = Personne.objects.all().order_by("nom", "prenom")

    serializer_class = PersonneSerializer

    # Protection des opérations CRUD
    permission_classes = [IsPersonneAdmin]

    # Configuration des filtres
    filter_backends = [DjangoFilterBackend]

    filterset_class = PersonneFilter

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(
            {
                "message": "Personne créée avec succès.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop("partial", False)

        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(
            {
                "message": "Personne modifiée avec succès.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        instance.delete()

        return Response(
            {
                "message": "Personne supprimée avec succès."
            },
            status=status.HTTP_200_OK
        )
