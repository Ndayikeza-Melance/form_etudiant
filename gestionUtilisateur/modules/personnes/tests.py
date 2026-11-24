
from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Personne


class PersonneModelTest(TestCase):
    """
    Tests du modèle Personne.
    """

    def setUp(self):
        self.personne = Personne(
            nom="Ndayizeye",
            prenom="Jean",
            telephone="+25769123456",
            email="jean@example.com",
            date_naissance=date(1995, 5, 10),
            nationalite="Burundaise",
            role="UTILISATEUR",
            type_personne="PHYSIQUE",
        )

        self.personne.set_password("TestPassword123!")
        self.personne.save()

    def test_creation_personne(self):
        self.assertEqual(self.personne.nom, "Ndayizeye")
        self.assertEqual(self.personne.prenom, "Jean")

    def test_str_personne(self):
        self.assertEqual(
            str(self.personne),
            "Ndayizeye Jean"
        )

    def test_hachage_mot_passe(self):
        self.assertNotEqual(
            self.personne.mot_passe,
            "TestPassword123!"
        )

    def test_verification_mot_passe(self):
        self.assertTrue(
            self.personne.check_password("TestPassword123!")
        )

    def test_mauvais_mot_passe(self):
        self.assertFalse(
            self.personne.check_password("MauvaisMotPasse")
        )

    def test_mot_passe_vide(self):
        with self.assertRaises(ValueError):
            self.personne.set_password("")

    def test_email_unique(self):
        with self.assertRaises(ValidationError):
            Personne.objects.create(
                nom="Test",
                prenom="Utilisateur",
                telephone="+25769123457",
                email="jean@example.com",
                date_naissance=date(1998, 1, 1),
                nationalite="Burundaise",
                role="UTILISATEUR",
                type_personne="PHYSIQUE",
                mot_passe="hash_test",
            )

    def test_telephone_unique(self):
        with self.assertRaises(ValidationError):
            Personne.objects.create(
                nom="Test",
                prenom="Utilisateur",
                telephone="+25769123456",
                email="test@example.com",
                date_naissance=date(1998, 1, 1),
                nationalite="Burundaise",
                role="UTILISATEUR",
                type_personne="PHYSIQUE",
                mot_passe="hash_test",
            )
