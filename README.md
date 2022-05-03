# Ristinolla

Tarvitsee python version 3.8 toimiakseen.
Toimii Pygame kirjaston avulla.

## Dokumentaatio

[Changelog](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/changelog.md)

[Vaativuusmaarittely](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/tuntikirjanpito.md)

[Käyttöohje](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/kayttoohje.md)

[Arkkitehtuuri](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/arkkitehtuuri.md)

## Asennukseen vaadittavat komennot

Asenna python 3.8

1. Käytä git clone (Github linkki tälle repositiolle) komentoa, jos haluat tämän koodin itsellesi.
2. poetry install

Nyt kaikki tarvittava pitäisi olla asennettuna!

## Komentorivillä komennot

#### Käynnistyy komennolla 

poetry run invoke start

#### Testaus komennolla

poetry run invoke test

#### Testikattavuusraportti komennolla

poetry run invoke coverage coverage-report

#### Pylint testaus komennolla

poetry run invoke lint
