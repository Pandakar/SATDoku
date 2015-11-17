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
			
# WORKS IN 3.3
# NEED TO TRANSLATE TO 2.7
def main():
	# Verify we have a puzzle (or set of puzzles) to solve
	if len(argv) < 2:
		print("Usage of program: 'py miniSAT.py <puzzle>'")
		print("<puzzle> can be an in-line puzzle from the command line, or the name of a file containing one or more puzzles.")
		exit()
	# Attempt to open the file
	# For now, just echoes all contents of file
	set_puzzles = {}
	n = 9*9
	num_puzzles = 0
	curr = ""
	if os.path.exists(argv[1]):
		try:
			puzzles = open(argv[1], 'r')
			# Loop through all the lines of the puzzle, read each individual character
			# If the character is not a newline or a blank space and is in the set [1,9] or is [0, *, ., ?]
			# read it into our current puzzle.
			# After 9x9 characters (81) characters, store puzzle in dictionary and start a new one.
			while True:
				c = puzzles.read(1)
				# break if character can't be read or we're at EOF
				if not c:
					break
				else:
					# if it's an int, read it
					try:
						if 0 <= int(c) <= 9:
							n -= 1
							curr += c
					except ValueError:
						# if it's a defined yet unknown symbol, read it
						if c == "." or c == "?" or c == "*":
							n -= 1
							curr += c
						# if it's ANYTHING else, just pass over it
						else:
							pass
					# if we've read 81 characters, we have a puzzle!
					# add puzzle to our set of puzzles
					if n == 0:
						set_puzzles[num_puzzles] = curr
						n = 9*9
						curr = ""
						num_puzzles += 1
				
		except IOError:
			print("Error in opening " + argv[1])
			print("Verify the file exists and/or the correct permissions are set for this file.")
			exit()
	else:
		print (argv[1])
		
	n = 0
	# For each puzzle:
	while n < num_puzzles:
		translate_puzzle()
		solved = solve_cnf_puzzle()
		if solved:
			print("Puzzle solution is pictured below.")
		else:
			print("Minimal encoding failed. Partial solution is below.")
		output_solved_puzzle(set_puzzles[n])
		n += 1
	
if __name__ == "__main__":
	main()
