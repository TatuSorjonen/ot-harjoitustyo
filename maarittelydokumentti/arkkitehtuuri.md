# Arkkitehtuuri

## Käyttöliittymä

Sovellus avaa pygamen avulla ikkunan pelille ja pelin loputtua ilmoittaa voittajan tai tasapelin

## Rakenne

Koostuu main-ohjelmasta ja kolmesta eri luokasta
- Luokka TicTacToe on käyttöliittymä, jossa ohjelma tapahtuu
- Luokka Board on lauta, johon voi mahdollisesti lisätä myöhemmin muita laudalla toimivia pelejä halutessaan
- Luokka TicTacToeBoard on tictactoe lauta, joka omaa kaikki tictactoelle tyypilliset piirteet

#### Sekvenssikaavio luokista ja niiden muuttujista


```mermaid
 classDiagram
      TicTacToe --> Board
      Board --> TicTacToeBoard
      Board --> Result
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
  tictactoe->> board: Testi
  board->>tictactoeboard: Testi2
```
