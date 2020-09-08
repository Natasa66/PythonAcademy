from unittest import TestCase
from Lesson8.birth_number import BirthNumber


class TestBirthNumber(TestCase):
    def test_validate_rc_platne_zena(self):
        bn = BirthNumber("1151012236")
        self.assertTrue(bn.validate_rc())

    def test_validate_rc_platne_muz(self):
        bn = BirthNumber("1101015333")
        self.assertTrue(bn.validate_rc())

    def test_validate_rc_neplatne_neexistujuci_datum(self):
        bn = BirthNumber("1121015698")
        self.assertFalse(bn.validate_rc())

    def test_validate_rc_neplatne_nedelitelne11(self):
        bn = BirthNumber("1151017055")
        self.assertFalse(bn.validate_rc())

    def test_validate_rc_platne_9_miestne(self):
        bn = BirthNumber("1101015333")
        self.assertTrue(bn.validate_rc())

    def test_validate_rc_neplatne_9_miestne_zly_datum(self):
        bn = BirthNumber("1102295333")
        self.assertFalse(bn.validate_rc())

    def test_get_birth_date(self):
        bn = BirthNumber("1101015333")
        self.assertEqual("01.01.2011", bn.get_birth_date())

    def test_get_age(self):
        bn = BirthNumber("1101015333")
        self.assertEqual(9, bn.get_age())

    def test_generate_bn(self):
        bn = BirthNumber("1101015333")
        generated = bn.generate_bn("10.11.1993", "female")
        self.assertTrue(BirthNumber(generated).validate_rc())