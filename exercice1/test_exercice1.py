import unittest

from evaluation.exercice1.exercice1 import join, average


class Test_Exercice_1(unittest.TestCase):
    def test_list_work(self):
        value = join(['Hello', "World"], " ")
        self.assertEqual("Hello world", value)

    def test_list_is_empty(self):
        value = join([], " ")
        self.assertEqual("", value)

    def test_list_wrong(self):
        with self.assertRaises(TypeError):
            join(3, " ")

    # test Moyenne
    def test_average_work(self):
        value = average([5, 10, 15])
        self.assertEqual(10, value)

    def test_average_is_empty(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    def test_average_wrong(self):
        with self.assertRaises(TypeError):
            average(["Wrong"])

