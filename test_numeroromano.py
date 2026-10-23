import unittest

import numeroromano as nr


class TestConverteNumeroRomano(unittest.TestCase):
    def test_i(self):
        self.assertEqual(nr.converte("I"), 1)

    def test_v(self):
        self.assertEqual(nr.converte("V"), 5)

    def test_ii(self):
        self.assertEqual(nr.converte("II"), 2)

    def test_xxii(self):
        self.assertEqual(nr.converte("XXII"), 22)

    def test_ix(self):
        self.assertEqual(nr.converte("IX"), 9)

    def test_xxiv(self):
        self.assertEqual(nr.converte("XXIV"), 24)


if __name__ == "__main__":
    unittest.main()
