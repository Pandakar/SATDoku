#!/bin/bash
# Script to help with automated testing of Sudoku puzzles
# Run in terminal window as 'bash autodoku.sh [file]
# [file] is of form: {123456789}*9 (i.e. a 81-character string)
# e.g. > bash autodoku.sh single.txt
# Script loops through each line in the file (presumes strings follow format) and for each line:
#	- runs it through sudokuToSAT to produce puzzle.cnf
#	- runs puzzle.cnf through minisat to produce puzzle.out
#	- runs puzzle.out through printSolution.py to get final result
# to-do: add stats tracking (puzzles inputted, puzzles solved, slowest puzzle, fastest puzzle, average time for puzzle)
while IFS='' read -r line || [[ -n "$line" ]]; do
	python sudokuToSAT.py $line --inline
	minisat puzzle.cnf puzzle.out > /dev/null
	python printSolution.py puzzle.out
done < "$1"
