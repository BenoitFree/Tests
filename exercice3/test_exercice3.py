import unittest

import self as self

from evaluation.exercice3.exercice3 import saut_de_ligne, saut_de_ligne_v2, saut_de_ligne_v3


class Test_saut_de_ligne(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(TypeError):
            saut_de_ligne("hello world", "lorem ipsum")

    def test_1(self):
        with self.assertRaises(TypeError):
            saut_de_ligne(123, 20)


#class Test_saut_de_ligne_V2(unittest.TestCase):
    #def ee(self):


class Test_saut_de_ligne_V3(unittest.TestCase):
    text = "Lestestsunitairespeuventmepermettredevérifier"
    with self.assertRaises(ValueError):
        saut_de_ligne_v3(text, 20)

    def test_work(self):
        text = "J’aimerai découper cette ligne: Cette ligne est beaucoup trop longue alors je souhaite la découper."
        value = saut_de_ligne_v3(text, 20)
        result = "J’aimerai découper cette ligne: Cette ligne est beaucoup trop longue alors je souhaite la découper."


if __name__ == '__main__':
    unittest.main()

 # Je n'ai pas réussi cet exercice