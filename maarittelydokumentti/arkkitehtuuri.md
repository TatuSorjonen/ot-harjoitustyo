# Arkkitehtuuri

## Käyttöliittymä

Sovelluksen käyttöliittymä on tehty StartMenu ja TicTacToe luokkien ympärillä.

- Pelin aloitusruutu (StartMenu)
- Ristinolla peli (TicTacToe)

TicTacToe luokka pitää huolen siitä, että aloitusruutu ja pygame ikkuna avautuvat oikeissa kohtaa

Kun peli aloitetaan kutsumalla TicTacToe luokan run() metodia se avaa StartMenu luokan avulla ikkunan, johon käyttäjä voi syöttää pelin aloitusarvot: laudan ruutujen määrä ja pelaajien nimet. TicTacToe luokka tarkistaa, ovatko annetut arvot oikein. Jos ovat, käynnistää itse pelin. Pelin aikana käyttäjä voi tallentaa pelin, ladata aikaisemmin tallennetun pelin tai lopettaa pelin. Pelit tallennetaan tiedostoihin, joiden pääte on .ttt (TicTacToe), ja tämän myötä vain .ttt päätteiset tiedostot avautuvat ohjelmassa. Käyttöliittymä ilmoittaa Tkinter luokan avaaman popup ikkunan avulla onnistuiko tallenus7lataus operaatio.

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

Lataus on toteutettu samoin kuin tallennus, mutta käytetään Tkinter kirjaston fliedialog.askopenfilename() funktiota:\n
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

Pelin käynnistettyä TicTacToe luokka kutsuu StartMenu luokan funktiota show(), joka avaa ruudun laudan ruutujen määrän määrittelylle ja pelaajien nimeämiselle. TicTacToe luokka tarkastaa ovatko arvot oikein. Jos huomataan arvojen virheellisyys, ohjelma palaa aloitusruutuun. Muuten peli alkaa normaalisti ja pygame ikkuna avautuu 


#### Pelin pelaaminen

```mermaid
sequenceDiagram
  actor Player1
  actor Player2
  participant TicTacToe
  participant TicTacToeBoard
  participant StartMenu
  TicTacToe->> TicTacToe: play_game()
  Player1->> TicTacToe: set_xo(mouse_x, mouse_y)
  TicTacToe->> TicTacToeBoard: add_x(x_square, y_square)
  TicTacToe->> TicTacToe: check_situation()
  Player2->> TicTacToe: set_xo(mouse_x, mouse_y)
  TicTacToe->> TicTacToeBoard: add_0(x_square, y_square)
  TicTacToe->> TicTacToe: check_situation()
  TicTacToe->> TicTacToe: set_winner()
  TicTacToe->> StartMenu: show()
```
