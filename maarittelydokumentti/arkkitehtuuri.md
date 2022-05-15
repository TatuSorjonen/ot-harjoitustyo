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

```mermaid
sequenceDiagram
  participant TicTacToe
  participant StartMenu
  TicTacToe->> StartMenu: create(StartMenu)
  StartMenu->> TicTacToe: Send(information)
  TicTacToe->> TicTacToe: Check(information)
  TicTacToe->> StartMenu: Send(fail information), if player name too long or small
```
