"""
miniSAT

University of Victoria
Computer Science 320, Fall 2015
"""

import os
from sys import exit, argv
#####
# (1) Sudoku Puzzle -> CNF Formula
#####
def translate_puzzle():
	pass
#####
# (2) CNF Formula -> Solver
#  Return: solution string representing puzzle
#####
def solve_cnf_puzzle():
	pass
#####
# (3) Solved Puzzle -> Readable Format
# NOTE ----- USED 3.3 TO PRINT SECTION
# UPDATE TO 2.7
# INPUT: Input string is of form (abcdefghi)*9 where [a, i] are unique integers in the set [1,9]
# This input string is essentially the same as the input string we use to solve the puzzle.
# Main difference is that this string (should) represent the solved version of the puzzle.
# OUTPUT: prints a 3x3 grid representation of the solved puzzle in ASCII to the console 
#
#####
def output_solved_puzzle(solved_puzzle):
	n = 9
	# Split input string of a single line into 9 lines for easier printing
	puzzle = [solved_puzzle[i:i+n] for i in range(0, len(solved_puzzle), n)]
	n = 3
	print("|" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "|")
	# Loop over all lines in puzzle and print in a nice ASCII format
	for line in puzzle:
		print("| " + line[0] + " " + line[1] + " " + line[2] + " | " + line[3] + " " + line[4] + " " + line[5] + " | " + line[6] + " " + line[7] + " " + line[8] + " |")
		n -= 1
		# Every 3 lines, print an intermediary line to split up the grid
		if n == 0:
			print("|" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "|")
			n = 3
def main():
	# Verify we have a puzzle (or set of puzzles) to solve
	if len(argv) < 2:
		print "Usage of program: 'py miniSAT.py <puzzle>'"
		print "<puzzle> can be an in-line puzzle from the command line, or the name of a file containing one or more puzzles."
		exit()
	# Attempt to open the file
	# For now, just echoes all contents of file
	if os.path.exists(argv[1]):
		try:
			puzzles = open(argv[1], 'r')
			for line in puzzles:
				print line
		except IOError:
			print "Error in opening " + argv[1]
			print "Verify the file exists and/or the correct permissions are set for this file."
			exit()
	else:
		print argv[1]
		
		
	
if __name__ == "__main__":
	main()
