# Ristinolla

HUOM! En kerennyt tekemään laskareita, jotka eivät kuulu harjoitustyöhön viikosta 3. Otan L (0 pistettä) tästä viikosta niiden osalta.

Tarvitsee Python version 3.8 toimiakseen.
Toimii Pygame kirjaston avulla.

## Dokumentaatio

[Changelog](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/changelog.md)

[Vaativuusmaarittely](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/TatuSorjonen/ot-harjoitustyo/blob/main/maarittelydokumentti/tuntikirjanpito.md)

## Tarvii asennukseen komennot

Asenna python 3.8 ja poetry

1. Käytä git clone (Github linkki tälle repositiolle) komentoa, jos haluat tämän koodin itsellesi.
2. poetry init --python "^3.8"
3. poetry install
4. poetry shell
5. poetry add cowsay
6. poetry add pytest --dev
7. poetry add coverage --dev
8. poetry add invoke

Nyt kaikki tarvittava pitäisi olla asennettuna!

## Komentorivillä invokella komennot

#### Käynnistyy komennolla 

poetry run invoke start

#### Testaus komennolla

poetry run invoke test

#### Testikattavuusraportti komennolla

poetry run invoke coverage coverage-report
