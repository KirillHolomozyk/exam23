import unittest

from main import arimethmetic_progression

class ArimethmeticProgressionTest(unittest.TestCase):

    def test_tenth_element(self):
        #десятий елемент прогресії
        a = 5
        d = 2
        n = 10
        expected = 23
        actual = arimethmetic_progression(a, d, n)
        self.assertEqual(expected, actual)

    def test_zero_values(self):
        #нульові значеннями
        a = 0
        d = 0
        n = 10
        expected = 0
        actual = arimethmetic_progression(a, d, n)
        self.assertEqual(expected, actual)

    def test_first_element(self):
          #значення першого елемента прогресії.
        a = 5
        d = 2
        n = 1
        expected = 5
        actual = arimethmetic_progression(a, d, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
