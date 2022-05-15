# Arkkitehtuuri

## Käyttöliittymä

Sovellus avaa pygamen avulla ikkunan pelille ja pelin loputtua ilmoittaa voittajan tai tasapelin

## Rakenne

Koostuu main-ohjelmasta ja neljästä eri luokasta
- Luokka TicTacToe on käyttöliittymä, jossa ohjelma tapahtuu
- Luokka TicTacToeBoard on ristinolla lauta, joka omaa kaikki ristinollalle tyypilliset piirteet
- Luokka Result pitää yllä missä vaiheessa peliä ollaan menossa

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

## Päätoiminnallisuudet

```mermaid
sequenceDiagram
  participant tictactoe
  participant board
  participant tictactoeboard
  tictactoe->> board: Foo
  board->>tictactoeboard: Foobar
```
