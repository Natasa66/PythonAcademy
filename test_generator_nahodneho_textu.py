from unittest import TestCase
from generator_nahodneho_textu import generator_nahodneho_textu, vytiahni_cisla_delitelne_dvomi


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
        self.assertEqual(len(result),5)


class TestVytiahniCislaDelitelneDvomi(TestCase):
    def test_vytiahni_cisla_delitelne_dvomi_int(self):
        result=vytiahni_cisla_delitelne_dvomi(5)
        self.assertFalse(result)

    def test_vytiahni_cisla_delitelne_dvomi_list(self):
        result=vytiahni_cisla_delitelne_dvomi([1,6,"greta6"])
        self.assertFalse(result)

    def test_vytiahni_cisla_delitelne_dvomi_tuple(self):
        result=vytiahni_cisla_delitelne_dvomi((1,6,"greta6"))
        self.assertFalse(result)

    def test_vytiahni_cisla_delitelne_dvomi_string(self):
        result=vytiahni_cisla_delitelne_dvomi("greta6")
        self.assertTrue(result)

    def test_vytiahni_cisla_delitelne_dvomi_correct_result(self):
        result=vytiahni_cisla_delitelne_dvomi("g123reta6K45Lnh76")
        self.assertEqual(result, [2,6,4,6,])
