import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_onko_olemassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_toimiiko_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100880)
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101280)

    def test_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riita_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kortti_toimii(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_kortilla_lounaat_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_saldoa(self):
        self.maksukortti.ota_rahaa(800)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.maksukortti.ota_rahaa(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortin_ja_kassapaatteen_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
