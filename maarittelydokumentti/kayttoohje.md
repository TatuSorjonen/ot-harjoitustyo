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

Jos kuitenkin jostain syystä laitat 0 tai yli 10 merkkiä pitkän nimen. Ilmoittaa ohjelma tästä seuraavalla tavalla:



#### Ristinollan idea

1. Molemmat pelaajat laittavat vuorotellen ristiä ja nollaa.
2. Pelaaja joka saa ensin neljänsuoran voittaa ja ruudulle ilmestyy voittaja
3. Jos peli päättyy tasan ohjelma ilmoittaa tasapelistä


Jos haluat pelata peliä uudestaan voit sulkea pelin oikealla ylhäällä olevasta raksista ja ajaa ohjelman uudestaan komennolla poetry run invoke start
