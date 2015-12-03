"""
printSolution
University of Victoria
Computer Science 320, Fall 2015
"""

import os
import sys
import math
from sys import exit, argv

def print_puzzle( split_puzzle, file_name ):
	n_root = round(math.pow( (len(split_puzzle)-1), 1.0/6))
	puzzle_solution = ""
	if math.pow( (n_root), 6 ) == len(split_puzzle)-1:
		n_root = int(n_root)
		n_size = n_root * n_root
		n_size = int(round(math.pow( (len(split_puzzle)-1), 1.0/3)))
		for i in split_puzzle:
			if int(i) > 0:
				puzzle_solution = puzzle_solution+str((int(i)-1)%9+1)
		output_solved_puzzle(puzzle_solution, n_root, n_size)
	else:
		print(file_name + " is not a valid miniSAT solution.")
		exit()

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
def output_solved_puzzle(solved_puzzle, n_root, n):
	# Split input string of a single line into 9 lines for easier printing
	puzzle = [solved_puzzle[i:i+n] for i in range(0, len(solved_puzzle), n)]
	print("+" + "-"*(n_root*2+1) + "+" + "-"*(n_root*2+1) + "+" + "-"*(n_root*2+1) + "+")
	counter = n_root
	# Loop over all lines in puzzle and print in a nice ASCII format
	for line in puzzle:
		print("| " + line[0] + " " + line[1] + " " + line[2] + " | " + line[3] + " " + line[4] + " " + line[5] + " | " + line[6] + " " + line[7] + " " + line[8] + " |")
		counter -= 1
		# Every 3 lines, print an intermediary line to split up the grid
		if counter == 0:
			print("+" + "-"*(n_root*2+1) + "+" + "-"*(n_root*2+1) + "+" + "-"*(n_root*2+1) + "+")
			counter = n_root

def main():

	# Verify we have a solution to print
	if len(argv) < 2:
		print("Usage of program: 'py printSolution.py [solution]'")
		print("[solution] is the file obtained by running 'puzzle.cnf' through a SAT solver.")
		exit()
	try:
		solution = open(argv[1], 'r')
		puzzle_solved = solution.readline()
		if puzzle_solved == "UNSAT\n":
			print "Puzzle was unsolvable."
		elif puzzle_solved == "SAT\n":
			split_puzzle = solution.readline().split(" ")
			print_puzzle( split_puzzle, argv[1] )
		else:
			print(argv[1] + " is not a valid miniSAT solution.")
			exit()
	except IOError:
		# Puzzle could not be opened, inform the user and end the program.
		print("Error in opening " + argv[1])
		print("Verify the file exists and/or the correct permissions are set for this file.")
		exit()

if __name__ == "__main__":
	main()
