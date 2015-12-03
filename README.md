# SATDoku

This project was made for partial completion of Computer Science 320, at the University of Victoria.
The SATDoku project takes a text version of a Sudoku puzzle and encodes it in conjunctive normal form to serve as input for a SAT solver.  
Group members: <insert names here later>

Two programs are included: `sudokuToSAT.py` and `printSolution.py`
<soon: bash script included for automated testing, presumes `minisat` is available on machine>

This program is compatible with Python 2.7. 

Usage: `py sudokuToSAT.py [input] [options]

```python
Options:

-e           | use extended encoding for puzzle
-g           |  encode puzzle in GSAT format
-h or --help | print this summary
--inline     | feed a 9x9 puzzle in place of file

Output is recorded in puzzle.cnf.
```

`input` can be in one of two forms:

1. A file containing a sudoku puzzle to solve. This file can have an arbitrary number of newlines and whitespace between characters. Characters are either in the set [1,9] as a given cell value, or are in the set {0, ., *, ?} of characters that represents unknown values. Example:
  ```bash
  py miniSAT.py easy_puzzle.txt [options]

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

  ```
2. A single line containing a puzzle. Example: 
  `py miniSAT.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300 --infile`

The current form of this program only covers the minimal encoding covered during lectures. 
Output is recorded in puzzle.cnf according to conjunctive normal form standards. 

For output as a grid, run:

`py printSolution.py [solution_file]`

This solution file is acquired by running puzzle.cnf through a SAT solver of your choice, and is printed in the following format:

```
+-------+-------+-------+
| 0 0 3 | 0 2 0 | 6 0 0 |
| 9 0 0 | 3 0 5 | 0 0 1 |
| 0 0 1 | 8 0 6 | 4 0 0 |
+-------+-------+-------+
| 0 0 8 | 1 0 2 | 9 0 0 |
| 7 0 0 | 0 0 0 | 0 0 8 |
| 0 0 6 | 7 0 8 | 2 0 0 |
+-------+-------+-------+
| 0 0 2 | 6 0 9 | 5 0 0 |
| 8 0 0 | 2 0 3 | 0 0 9 |
| 0 0 5 | 0 1 0 | 3 0 0 |
+-------+-------+-------+
```

where the grid contains the solved version of the given Sudoku puzzle. 
