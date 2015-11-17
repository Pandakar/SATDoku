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
#####
def output_solved_puzzle():
	pass
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
