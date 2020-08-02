from unittest import TestCase
from Cezarova_sifra import zasifruj_Cezar, rozsifruj_Cezar, brutal_force_Cezar


class TestCezarovaSifra(TestCase):
    def test_ceasar_cipher_standard(self):
        result = zasifruj_Cezar("ahoj svet!", 1)
        self.assertEqual(result, "bipk twfu!")

    def test_ceasar_cipher_upper_lower(self):
        result = zasifruj_Cezar("Ahoj Svet!", 1)
        self.assertEqual(result, "Bipk Twfu!")

    # def test_ceasar_cipher_index_more_than_26(self):
    #     result = zasifruj_Cezar("Ahoj Svet!", 27)
    #     result = zasifruj_Cezar("Ahoj Svet!", 287)
    #     self.assertFalse(result)

    def test_ceasar_cipher_index_less_than_0(self):
        result = zasifruj_Cezar("Ahoj Svet!", -2)
        result = zasifruj_Cezar("Ahoj Svet!", -200)
        self.assertFalse(result)

#     def test_ceasar_cipher_index_cross_z(self):
# @@ -28,7 +28,7 @@ def test_ceasar_cipher_special_chars(self):
#         self.assertEqual(result, " $#$*@#&$@#!?.,")

    def test_ceasar_cipher_non_text(self):
        result = zasifruj_Cezar(23,1)
        self.assertFalse(result)


# @@ -42,11 +42,11 @@ def test_ceasar_cipher_upper_lower(self):
#         self.assertEqual(result, "Ahoj Svet!")

    # def test_ceasar_cipher_index_more_than_26(self):
    #     result = rozsifruj_Cezar("Ahoj Svet!", 27)
    #     result = rozsifruj_Cezar("Ahoj Svet!", 277)
    #     self.assertFalse(result)

    def test_ceasar_cipher_index_less_than_0_rozsifruj(self):
        result = rozsifruj_Cezar("Ahoj Svet!", -2)
        result = rozsifruj_Cezar("Ahoj Svet!", -60)
        self.assertFalse(result)

    def test_ceasar_cipher_index_cross_z(self):
        result = rozsifruj_Cezar("ZzZzZz", 1)
        self.assertEqual(result, "YyYyYy")
    def test_ceasar_cipher_index_cross_a(self):
        result = rozsifruj_Cezar("AaAaAa", 1)
        self.assertEqual(result, "ZzZzZz")
    def test_ceasar_cipher_index_special_chars(self):
        result = rozsifruj_Cezar(" $#$*@#&$@#!?.,", 10)
        self.assertEqual(result, " $#$*@#&$@#!?.,")

class TestBruteForce(TestCase):
    def test_ceasar_cipher_standard(self):
        result = brutal_force_Cezar("bipk twfu!")
        self.assertTrue("ahoj svet!" in result)
        self.assertIsInstance(result, list)