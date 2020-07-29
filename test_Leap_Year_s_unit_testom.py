from unittest import TestCase
from Leap_Year_s_unit_testom import leapyear

class Test(TestCase):
    def test_leapyear_true_2000(self):
        result=leapyear(2000)    #toto by malo byt True
        self.assertTrue(result)

    def test_leapyear_false_2001(self):
        result = leapyear(2001)  # toto by malo byt False
        self.assertFalse(result)

    # def test_leapyear_false_1600(self):
    #     result = leapyear(1600)  # toto by malo byt False
    #     self.assertFalse(result)

    def test_leapyear_false_2100(self):
        result = leapyear(2100)  # toto by malo byt False
        self.assertFalse(result)

    def test_leapyear_true_2004(self):
        result=leapyear(2004)    #toto by malo byt True
        self.assertTrue(result)

    def test_leapyear_string(self):
        result = leapyear("dfa")  # False
        self.assertFalse(result)