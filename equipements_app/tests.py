
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from .models import (
    Equipement,
    TypeEquipement,
    StatutEquipement,
)

User = get_user_model()


class EquipementAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="agent",
            email="agent@example.com",
            password="TestPassword123!",
        )

        self.type_equipement = TypeEquipement.objects.create(
            nom="Routeur",
        )

        self.statut = StatutEquipement.objects.create(
            nom="Disponible",
        )

        self.url = "/api/v1/equipements/"

    def test_liste_sans_authentification(self):
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_liste_avec_authentification(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_creation_equipement(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "type_equipement": self.type_equipement.pk,
            "statut": self.statut.pk,
            "numero_serie": "ABC123",
            "device_id": "DEVICE001",
        }

        response = self.client.post(
            self.url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            Equipement.objects.filter(
                numero_serie="ABC123"
            ).exists()
        )

    def test_creation_numero_serie_duplique(self):
        Equipement.objects.create(
            type_equipement=self.type_equipement,
            statut=self.statut,
            numero_serie="ABC123",
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            self.url,
            {
                "type_equipement": self.type_equipement.pk,
                "statut": self.statut.pk,
                "numero_serie": "ABC123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
