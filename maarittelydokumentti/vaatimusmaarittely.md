## Vaatimusmäärittely ristinollalle

**Sovelluksen perimmäinen tarkoitus**

- Toimii samalla tavalla kuin normaali ristinolla, mutta pelataan neljän suoraan eikä kolmen suoraan. Vuorotellen laitetaan x ja o merkkejä ruudulle. 
- Pelaajat nimeävät itsensä (1-10 merkkiä) ja laudan koon (5-30 ruutua).
- Pelin aikana on myös mahdollista tallentaa peli ja ladata jonkin aikaisemman tallentamansa pelin tai sulkea pelin.

**Käyttäjä**

Peliä voi pelata kuka tahansa ilman kirjautumista. Myöhemmin voi mahdollisesti tehdä jonkinlaisen kirjautumisen

**Ristinollan toiminta**

- Pelaajat valitsevat nimet itselleen ja laudan koon. Tämän jälkeen voivat aloittaa pelin
- Jos pelaajat antavat liian lyhyen nimen tai liian pitkän nimen, peli ei ala ja ruudulle ilmestyy virheteksti
- Pelissä voittaja on se kumpi pelaaja saa ensin neljän suoran
- Pelaajat voivat tallentaa ja ladata pelin (Ilmoittaa onnistuiko vai ei)
- Sovellus ilmoittaa voittajasta ja palaa aloitusruudulle, jos jompikumpi voittaa

**Jatkoideoita**

- Kirjautumismahdollisuus käyttäjille
- Pisteytys
- Tkinter käyttöliittymäosioiden korvaaminen pygame toteutuksella
