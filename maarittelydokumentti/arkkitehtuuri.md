# Arkkitehtuuri

## Käyttöliittymä

Sovelluksen käyttöliittymä on tehty StartMenu ja TicTacToe luokkien ympärillä.

- Pelin aloitusruutu (StartMenu)
- Ristinolla peli (TicTacToe)

TicTacToe luokka pitää huolen siitä, että aloitusruutu ja pygame ikkuna avautuvat oikeissa kohtaa

Kun peli aloitetaan kutsumalla TicTacToe luokan run() metodia se avaa StartMenu luokan avulla ikkunan, johon käyttäjä voi syöttää pelin aloitusarvot: laudan ruutujen määrä ja pelaajien nimet. TicTacToe luokka tarkistaa, ovatko annetut arvot oikein. Jos ovat, käynnistää itse pelin. Pelin aikana käyttäjä voi tallentaa pelin, ladata aikaisemmin tallennetun pelin tai lopettaa pelin. Pelit tallennetaan tiedostoihin, joiden pääte on .ttt (TicTacToe), ja tämän myötä vain .ttt päätteiset tiedostot avautuvat ohjelmassa. Käyttöliittymä ilmoittaa Tkinter luokan avaaman popup ikkunan avulla onnistuiko tallenus/lataus operaatio.

## Rakenne

Ohjelma koostuu main-ohjelmasta ja neljästä eri luokasta
- Luokka TicTacToe on itse pelin käyttöliittymä, jossa käyttäjät voivat pelata ristinolla peliä
- Luokka TicTacToeBoard on tietorakenne, jossa pidetään yllä pelin tilaa
- Luokka Result on apuluokka, jossa on määritelty missä tilanteessa peli voi olla
- Luokka StartMenu on Tkinter kirjaston avulla toteutettu aloitusvalikko, jossa määritellään pelin aloitusparametrit: Laudan ruutujen määrä ja pelaajien nimet

#### Sekvenssikaavio luokista ja niiden luokkamuuttujista


```mermaid
 classDiagram
      TicTacToe --> TicTacToeBoard
      TicTacToe --> Result
      TicTacToe --> StartMenu
      TicTacToeBoard --> Result
      
      class TicTacToe{
          start_menu
          tictactoeboard
          screen
          x_image
          o_image
          square_size
          grid_size
          result_text
          whose_turn
          background_color
          grid_color
          bottom_height
          button_width
          running
      }
      class TicTacToeBoard{
          num_squares
          result
          player1
          player2
          board
          whose_turn
      }
      class Result{
          ONGOING
          DRAW
          FIRST_WIN
          SECOND_WIN
      }
      class StartMenu{
          root
          num_squares
          player1
          player2
          name_max_size
          window_width
          window_height
          previous_result
      }
```

## Tietojen pysyväistallennus

Tallennuksen pystyy tekemään pelin aikana vasemmalta alakulmasta 'Tallenna peli' nappia painamalla. Tämä tarkoittaa käytännössä, että lataat pelin koneellesi .ttt muotoon käyttäen Tkinter kirjaston filedialog.asksaveasfilename() funktiota:

![](./Kuvat/Tallennus.png)

Lataus on toteutettu samoin kuin tallennus, mutta käytetään Tkinter kirjaston fliedialog.askopenfilename() funktiota:
![](./Kuvat/Lataus.png)

Ohjelma antaa ilmoituksen, jos tallennus/lataus onnistui tai epäonnistui:  
![](./Kuvat/Tallennus_epaonnistui.png)

Epäonnistuminen on estetty try-except:llä, jotta ohjelma ei kaadu virheeseen, vaan heittää ainoastaan ilmoituksen asiasta.

## Päätoiminnallisuudet

#### Pelin aloittaminen

Peli aloitetaan index.py tiedoston main funktiosta, joka luo uuden TicTacToe luokan ilmentymän ja käynnistää pelin TicTacToe luokan run-funktiolla. Alla olevassa diagrammissa on kuvattu kuinka pelin aloittaminen etenee. 

```mermaid
sequenceDiagram
  participant index.py
  participant TicTacToe
  participant StartMenu
  index.py->> TicTacToe: run()
  TicTacToe->> StartMenu: show()
  StartMenu-->> TicTacToe: number of squares, player names
  TicTacToe->> TicTacToe: players_name_ok(max_size)
  TicTacToe->> StartMenu: show(), if player names too long or short
  TicTacToe->> TicTacToe: start_game()
```

Ohjelman käynnistettyä TicTacToe luokka kutsuu StartMenu luokan funktiota show(), joka avaa ruudun laudan ruutujen määrän määrittelylle ja pelaajien nimeämiselle. TicTacToe luokka tarkastaa ovatko arvot oikein. Jos huomataan arvojen virheellisyys, ohjelma palaa aloitusruutuun. Muuten peli alkaa normaalisti ja pygame ikkuna avautuu 


#### Pelin pelaaminen

Peliä pelataan TicTacToe luokassa play_game-funktion silmukkaa hyödyntäen. Alla olevassa diagrammissa on kuvattu kuinka peli etenee.

```mermaid
sequenceDiagram
  actor Player1
  actor Player2
  participant TicTacToe
  participant TicTacToeBoard
  participant StartMenu
  loop TicTacToe.play_game()
  Player1->> TicTacToe: set_xo(mouse_x, mouse_y)
  TicTacToe->> TicTacToeBoard: add_x(x_square, y_square)
  TicTacToe->> TicTacToe: check_situation()
  Player2->> TicTacToe: set_xo(mouse_x, mouse_y)
  TicTacToe->> TicTacToeBoard: add_0(x_square, y_square)
  TicTacToe->> TicTacToe: check_situation()
  end
  TicTacToe->> TicTacToe: set_winner()
  TicTacToe->> StartMenu: show()
```
Pelin käynnistettyä pelaajat painavat vuorotellen laudalla näkyviä ruutuja. Jokaisen painalluksen jälkeen laudalle asetetaan joko x tai o merkki, jos ruutu on tyhjä. Laudan tilaa pidetään yllä TicTacToeBoard luokassa. Ruudukon ulkopuolelle tehdyt klikkaukset eivät päivitä tietorakenteen tilaa. Jokaisen siirron jälkeen päivitetään ruudukko ja piirretään uusi tilanne. Lisäksi tarkastetaan onko voittaja löytynyt tai peli päättynyt tasapeliin. Jos on tai lauta on täynnä niin peli loppuu ja uusi StartMenu luokan avulla avattava aloitusruutu aukeaa.


#### Pelin lopettaminen

Pelin voi lopettaa kahdella eri tavalla. Alla olevassa diagrammissa on kuvattu mahdolliset lopetustavat

```mermaid
sequenceDiagram
  participant index.py
  participant TicTacToe
  participant StartMenu
  participant TicTacToeBoard
  index.py->> TicTacToe: run()
  TicTacToe->> StartMenu: show()
  StartMenu-->> TicTacToe: number of squares, player names
  TicTacToe-->> index.py: If number of squares = 0
  TicTacToe->> TicTacToe: play_game()
  TicTacToe->> TicTacToe: check_button_pressed()
  TicTacToe-->> index.py: If user clicked quit button
  TicTacToe->> TicTacToe: check_situation()
  TicTacToe->> StartMenu: show()
  StartMenu-->> TicTacToe: number of squares, player names
  TicTacToe-->> index.py: If number of squares = 0
```
Pelin voi lopettaa, joko painamalla start menun nappia 'Poistu' tai pygame ikkunassa kohdasta 'Lopeta peli'.

## Ohjelmaan jääneet heikkoudet

Tkinter kirjasto ei toimi täydellisesti yhteen pygamen kirjaston kanssa. Tkinter ikkunan avautuessa pygame kirjaston tapahtumakäsittelijä saattaa jossain tilanteessa luulla, että ohjema ei enää vastaa ja ilmoittaa tästä. Ilmoituksesta pääsee eroon painamalla 'Wait' tai 'Force Quit' painikkeita, joista jälkimmäinen sulkee ohjelman.
