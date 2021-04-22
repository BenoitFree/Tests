import unittest

from evaluation.exercice2.exercice2 import is_leap_year_v1, is_leap_year_v2, is_leap_year_v3


class LeapTestsV1(unittest.TestCase):
    def test_LeapTestsV1_is_true(self):
        value = is_leap_year_v1(2021)
        self.assertFalse(value)


class LeapTestsV2(unittest.TestCase):
    def test_LeapTestsV1_is_true(self):
        value = is_leap_year_v2(2021)
        self.assertFalse(value)

    def test_LeapTestsV2_is_m400(self):
        value = is_leap_year_v2(2000)
        self.assertTrue(value)

    def test_LeapTestsV2_is_not_m400(self):
        value = is_leap_year_v2(2020)
        self.assertFalse(value)


class LeapTestsV3(unittest.TestCase):
    def test_LeapTestsV1_is_true(self):
        value = is_leap_year_v3(2021)
        self.assertFalse(value)

    def test_LeapTestsV2_is_m400(self):
        value = is_leap_year_v3(2000)
        self.assertTrue(value)

    def test_LeapTestsV2_is_not_m400(self):
        value = is_leap_year_v3(2020)
        self.assertFalse(value)

    def test_LeapTestsV2_is_m100_is_not_m400(self):
        value = is_leap_year_v3(1900)
        self.assertFalse(value)

    def test_LeapTestsV2_is_m400_is_not_m100(self):
        value = is_leap_year_v3(2004)
        self.assertTrue(value)


if __name__ == '__main__':
    unittest.main()
