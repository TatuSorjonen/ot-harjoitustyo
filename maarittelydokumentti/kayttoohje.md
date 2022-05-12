## Käyttöohje

Voit ladata uusimman version [tästä](https://github.com/TatuSorjonen/ot-harjoitustyo/releases/tag/viikko6)

Ohjelma tarvitsee python 3.8 version toimiakseen

#### Tarvittavat komennot komentorivillä

1. poetry install
2. poetry run invoke start
3. Ruudulle käynnistyy ohjelma

#### Ohjelman käynnistettyä

Kun ohjelma käynnistetään syntyy aloitusruutu mistä valitaan laudan koko, pelaajien nimet ja aloitetaanko peli vai lopetetaanko.

![](./Kuvat/Aloitusruutu.png)

Kuvan mukaisesti voit valita laudan kooksi 5-30 ruutua ja vain 1-10 merkkisen nimen pelaajille.

Jos kuitenkin jostain syystä laitat 0 tai yli 10 merkkiä pitkän nimen kummalle tahansa. Ilmoittaa ohjelma tästä seuraavalla tavalla:

![](./Kuvat/Virhenimi.png)

Tämän jälkeen voit aloittaa pelin kun sinulla on kaksi pelaajaa nimettynä, painamalla 'Aloita peli' painikkeesta
pelille aukee ikkuna:

![](./Kuvat/Ristinolla.png)

Tässä ikkunassa voidaan vuorotellen painella ruutuja (Vuoro vaihtuu automaattisesti), kunnes toinen pelaaja saa neljän suoran tai lauta menee täyteen.

![](./Kuvat/Toisenvuoro.png)

Jos toinen pelaaja voittaa, peli palautuu aloitusvalikkoon ja ilmoittaa tuloksen:

![](./Kuvat/Voittaja.png)

Myös tasapelistä tekee saman:

![](./Kuvat/Tasapeli.png)

Voit aloittaa pelin niin monta kertaa kuin jaksat

Kun et enää jaksa pelata, voit lopettaa pelin painamalla 'Poistu' painiketta
