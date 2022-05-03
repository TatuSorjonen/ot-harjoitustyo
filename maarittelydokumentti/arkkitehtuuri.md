```mermaid
 classDiagram
      TicTacToe "*" --> "1"  Board "*" --> "1" TicTacToeBoard
      class TicTacToe{
          username
          password
      }
      class Board{
          id
          content
          done
      }
      class TicTacToeBoard{
          id
          content
          done
      }
```



```mermaid
sequenceDiagram
  participant ui
  participant board
  participant tictactoeboard
  ui->> board: Testi
  board->>tictactoeboard: Testi2
```
