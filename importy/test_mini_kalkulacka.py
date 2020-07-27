from unittest import TestCase
from importy.mini_kalkulacka import spocitaj


class TestSpocitaj(TestCase):
    def test_spocitaj_int_1_2(self):
        result = spocitaj(1, 2)
        self.assertEqual(result, 3)

    def test_spocitaj_int_minus4_minus4(self):
        result = spocitaj(-4, -4)
        self.assertEqual(result, -8)

    def test_spocitaj_int_minus4_4(self):
        result = spocitaj(-4, 4)
        self.assertEqual(result, 0)

    def test_spocitaj_str_str(self):  # stringy by nemal spocitavat
        result = spocitaj("ahoj, ", "svet")
        self.assertFalse(result)

    def test_spocitaj_str_int(self):  # ani cislo a string nema byt spocitane
        result = spocitaj("ahoj, ", 5)
        self.assertFalse(result)

    def test_spocitaj_int_str(self):  # ani cislo a string nema byt spocitane
        result = spocitaj(12, "bus")
        self.assertFalse(result)

    def test_spocitaj_return_int(self):  # vrati vzdy integer
        result = spocitaj(3, 5)
        self.assertIsInstance(result,int)

