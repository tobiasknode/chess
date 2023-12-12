import unittest
from Spieler import Spieler


class TestSpieler(unittest.TestCase):
    def test_get_farbe(self):
        spieler = Spieler("Hans", "w")
        self.assertEqual(spieler.get_farbe(), "w")

    def test_get_name(self):
        spieler = Spieler("Hans", "w")
        self.assertEqual(spieler.get_name(), "Hans")


if __name__ == "__main__":
    unittest.main()
