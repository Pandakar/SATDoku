# SATDoku

This project was made for partial completion of Computer Science 320, at the University of Victoria.
The SATDoku project takes a text version of a Sudoku puzzle, converts it to a minimal encoding of conjunctive normal form, and solves it.  
Group members: <insert names here later>

miniSAT.py is intended to be run in Python 2.7. <currently runs in 3.3, final version will be guaranteed to work in 2.7>
Run miniSAT.py from the command line as

`py miniSAT.py input`

`input` can be in one of two forms:

1. A file containing sudoku puzzles to solve. This file can have an arbitrary number of newlines and whitespace between characters. Characters are either in the set [1,9] as a given cell value, or are in the set {0, ., *, ?} of characters that represents unknown values. Example:
  ```bash
  py miniSAT.py easy_puzzles.txt

  easy_puzzles.txt:
  200080300 
  060070084
  030500209
  000105408
  000000000
  402706000
  301007040
  720040060
  004010003

  000000907
  000420180
  000705026
  100904000
  050000040
  000507009
  920108000
  034059000
  507000000
  ```
2. A single line containing a puzzle. Example: 
  `py miniSAT.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300`

The current form of this program only covers the minimal encoding covered during lectures. 
Output is given in the following form:

```
|-------+-------+-------|
| 0 0 3 | 0 2 0 | 6 0 0 |
| 9 0 0 | 3 0 5 | 0 0 1 |
| 0 0 1 | 8 0 6 | 4 0 0 |
|-------+-------+-------|
| 0 0 8 | 1 0 2 | 9 0 0 |
| 7 0 0 | 0 0 0 | 0 0 8 |
| 0 0 6 | 7 0 8 | 2 0 0 |
|-------+-------+-------|
| 0 0 2 | 6 0 9 | 5 0 0 |
| 8 0 0 | 2 0 3 | 0 0 9 |
| 0 0 5 | 0 1 0 | 3 0 0 |
|-------+-------+-------|
```

where the grid contains the solved version of an inputted Sudoku puzzle. 
