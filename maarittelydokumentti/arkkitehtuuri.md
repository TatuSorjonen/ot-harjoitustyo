# Arkkitehtuuri

## Käyttöliittymä

Sovelluksen käyttöliittymä on tehty StartMenu ja TicTacToe luokkien ympärillä.

- Pelin aloitusruutu (StartMenu)
- Ristinolla peli (TicTacToe)

TicTacToe luokka pitää huolen siitä, että aloitusruutu ja pygame ikkuna avautuvat oikeissa kohtaa

Kun peli aloitetaan StartMenu luokasta, TicTacToe luokka tarkistaa, onko arvot oikein. Jos ovat, avaa itse pelin, josta taas voi tallentaa ja ladata pelin halutessaan. Pelin tallennuksessa se tallentuu .ttt tiedostossa, ja tämän myötä vain .ttt päätteiset tiedostot avautuvat ohjelmassa. Ui ilmoittaa onnistuiko tallennus tai lataus Tkinterin omalla ilmoitusruudulla.

## Rakenne

Koostuu main-ohjelmasta ja neljästä eri luokasta
- Luokka TicTacToe on käyttöliittymä, jossa ohjelma tapahtuu
- Luokka TicTacToeBoard on ristinolla lauta, joka omaa kaikki ristinollalle tyypilliset piirteet
- Luokka Result pitää yllä missä vaiheessa peliä ollaan menossa
- Luokka StartMenu on luokka, missä pidetään yllä aloitusruutua

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

Latauksessa on sama, mutta käytetään Tkinter kirjaston fliedialog.askopenfilename() funktiota:
![](./Kuvat/Lataus.png)

Ohjelma antaa ilmoituksen, jos tallennus/lataus onnistui tai epäonnistui

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
