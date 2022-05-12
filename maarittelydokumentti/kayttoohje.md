## Käyttöohje

Voit ladata uusimman version [tästä](https://github.com/TatuSorjonen/ot-harjoitustyo/releases/tag/viikko6)

Ohjelma tarvitsee python 3.8 version toimiakseen

#### Tarvittavat komennot komentorivillä

1. poetry install
2. poetry run invoke start
3. Ruudulle käynnistyy ohjelma

#### Ohjelman käynnistäminen

Kun ohjelma käynnistetään syntyy aloitusruutu mistä valitaan laudan koko, pelaajien nimet ja aloitetaanko peli vai lopetetaanko.

![](./Kuvat/Aloitusruutu.png)

Kuvan mukaisesti voit valita laudan kooksi 5-30 ruutua ja vain 1-10 merkkisen nimen pelaajille.

Jos kuitenkin jostain syystä laitat 0 tai yli 10 merkkiä pitkän nimen kummalle tahansa. Ilmoittaa ohjelma tästä seuraavalla tavalla:



Tämän jälkeen voit aloittaa pelin kun sinulla on kaksi pelaajaa nimettynä painamalla 'Aloita peli' painikkeesta
Pelille aukee ikkuna:


Tässä ikkunassa voidaan vuorotellen painella ruutuja (Vuoro vaihtuu automaattisesti), kunnes toinen pelaaja saa neljän suoran tai lauta menee täyteen.

Jos toinen pelaaja voittaa peli palautuu aloitusvalikkoon ja ilmoittaa tuloksen:


Myös tasapelistä tekee saman:

Kun et enää jaksa pelata, voit lopettaa pelin painamalla 'Poistu' painiketta


#### Ristinollan idea

1. Molemmat pelaajat laittavat vuorotellen ristiä ja nollaa.
2. Pelaaja joka saa ensin neljänsuoran voittaa ja ruudulle ilmestyy voittaja
3. Jos peli päättyy tasan ohjelma ilmoittaa tasapelistä


Jos haluat pelata peliä uudestaan voit sulkea pelin oikealla ylhäällä olevasta raksista ja ajaa ohjelman uudestaan komennolla poetry run invoke start
