import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.06")

    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
