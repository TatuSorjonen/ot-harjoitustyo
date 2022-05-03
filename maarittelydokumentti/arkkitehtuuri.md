# Arkkitehtuuri

## Käyttöliittymä

Sovellus avaa pygamen avulla ikkunan pelille ja pelin loputtua ilmoittaa voittajan tai tasapelin

## Rakenne

Koostuu main-ohjelmasta ja neljästä eri luokasta
- Luokka TicTacToe on käyttöliittymä, jossa ohjelma tapahtuu
- Luokka Board on lauta, johon voi mahdollisesti lisätä myöhemmin muita laudalla toimivia pelejä halutessaan
- Luokka TicTacToeBoard on Board luokan aliluokka ja on ristinolla peli, joka omaa kaikki ristinollalle tyypilliset piirteet
- Luokka Result pitää yllä missä vaiheessa peliä ollaan menossa

#### Sekvenssikaavio luokista ja niiden luokkamuuttujista


```mermaid
 classDiagram
      TicTacToe --> TicTacToeBoard
      TicTacToe --> Result
      TicTacToeBoard --> Board
      TicTacToeBoard --> Result
      
      class TicTacToe{
          board
          grid_size
          num_squares
          square_size
      }
      class Board{
          num_squares
          board
          result
      }
      class TicTacToeBoard{
          board
          whose_turn
          winner
      }
      class Result{
          ONGOING
          DRAW
          FIRST_WIN
          SECOND_WIN
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
