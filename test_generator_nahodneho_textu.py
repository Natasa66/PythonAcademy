from unittest import TestCase
from generator_nahodneho_textu import generator_nahodneho_textu


class TestGeneratorNahodnehoTextu(TestCase):
    def test_generator_nahodneho_textu_string(self):
        result = generator_nahodneho_textu("abs")
        self.assertFalse(result)

    def test_generator_nahodneho_textu_list(self):
        result = generator_nahodneho_textu([1])
        self.assertFalse(result)

    def test_generator_nahodneho_textu_zero(self):
        result = generator_nahodneho_textu(0)
        self.assertFalse(result)

    def test_generator_nahodneho_textu_True(self):
        result = generator_nahodneho_textu(5)
        self.assertIsInstance(result, str)