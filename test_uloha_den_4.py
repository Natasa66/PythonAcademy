from unittest import TestCase
from uloha_den_4 import zacina_samohlaskou


class TestZacinaSamohlaskou(TestCase):
    def test_zacina_samohlaskou_male_pismena_true(self):
        result = zacina_samohlaskou("alena")
        self.assertTrue(result)

    def test_zacina_samohlaskou_velke_pismena_true(self):
        result = zacina_samohlaskou("Alena")
        self.assertTrue(result)

    def test_zacina_samohlaskou_male_pismena_false(self):
        result = zacina_samohlaskou("lenka")
        self.assertFalse(result)

    def test_zacina_samohlaskou_velke_pismena_false(self):
        result = zacina_samohlaskou("Lenka")
        self.assertFalse(result)

    def test_zacina_samohlaskou_nie_je_retazec_false(self):
        result = zacina_samohlaskou(45)
        self.assertFalse(result)