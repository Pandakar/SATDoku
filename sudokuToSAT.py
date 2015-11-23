"""
sudokuToSAT
University of Victoria
Computer Science 320, Fall 2015
"""

import os
import sys
import math
from sys import exit, argv

class ID_Node:
	def __init__(self, character=None, id=None, next=None):
		self.character = character
		self.id = id
		self.next  = next

class Entry_Node:
	def __init__(self, location=None, id=None, next=None):
		self.location = location
		self.id = id
		self.next  = next

def get_character_ID( head, character ):
	node = head
	if head == -1:
		return -1
	while node:
		if node.character == character:
			return node.id
		node = node.next
	return -1

def new_character_ID( tail, id, character ):
	node = ID_Node(character, id)
	if tail != -1:
		tail.next = node
	return node

def get_fix_character_ID( head, id ):
	node = head
	if head == -1:
		return -1
	while node:
		if node.id == id:
			try:
				
				return int(node.character)
			except ValueError:
				print 'fatal error, id given is not connected to an integer value'
		node = node.next
	return -1

def fix_character_ID( puzzle_head, id_head ):
	node = puzzle_head
	while node:
		node.id = get_fix_character_ID( id_head, node.id )
		node = node.next

def print_node(head):
	node = head
	while node:
		# print node.location
		print node.id
		#print node.character
		node = node.next

def main():
	charactersScanned = 0
	num_puzzle = 0
	curr = ""
	head = -1
	tail = -1
	new_ID = 1
	known_values_head = -1
	known_values_tail = -1
	ints_found = 0
	number_of_known_values = 0
	skip_meta = False

	# Verify we have a puzzle (or set of puzzles) to solve
	if len(argv) < 2:
		print("Usage of program: 'py miniSAT.py <puzzle>'")
		print("<puzzle> can be an in-line puzzle from the command line, or the name of a file containing a puzzle.")
		exit()

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
					cInt = c
					# if it's an int, read it
					try:
						if 1 <= int(cInt) <= 9:
							charactersScanned += 1
							# get id
							current_ID = get_character_ID( head, c )
							if current_ID == -1:
								node = new_character_ID(tail, new_ID, c)
								current_ID = new_ID
								new_ID += 1
								tail = node
								# make new id node
								if head == -1:
									head = node
								ints_found += 1
							node = Entry_Node(charactersScanned, current_ID)
							if known_values_head == -1:
								known_values_head = node
							else:
								known_values_tail.next = node
							known_values_tail = node
							number_of_known_values += 1


						else:
							charactersScanned+=1


					except ValueError:
						# if it's a defined yet unknown symbol, read it
						if c == "." or c == "?" or c == "*":
							charactersScanned += 1
						# if it's ANYTHING else, just pass over it
						elif ( c =="\n" or c =="\s" or c =="\r" or c == "\t" ):
							pass
						else:
							charactersScanned += 1
							current_ID = get_character_ID( head, c )
							if current_ID == -1:
								node = new_character_ID(tail, new_ID, c)
								new_ID += 1
								tail = node
								# make new id node
								if head == -1:
									head = node
							node = Entry_Node(charactersScanned, current_ID)
							if known_values_head == -1:
								known_values_head = node
							else:
								known_values_tail.next = node
							known_values_tail = node
							number_of_known_values += 1
		except IOError:
			print("Error in opening " + argv[1])
			print("Verify the file exists and/or the correct permissions are set for this file.")
			exit()
	else:
		print (argv[1])
	# print charactersScanned
	nCheck = math.pow( (charactersScanned), 1.0/4)
	if nCheck*nCheck == 9 and ints_found == 9:
		fix_character_ID(known_values_head, head)
		skip_meta = True
		# fix ids

	if (nCheck).is_integer() and math.pow( (nCheck), 4 ) == charactersScanned and (nCheck*nCheck + 1) >= new_ID:
		print 'Valid Puzzle'
		try:
			meta_file = open('sudoku.meta', 'w')
			if skip_meta == True:
				meta_file.write( 'Skip Meta')
			else:
				node = head
				while node:
					meta_file.write( node.character )
					meta_file.write( ' ' )
					node = node.next
		except IOError:
			print("Error in opening " + argv[1])
			print("Verify the file exists and/or the correct permissions are set for this file.")
			exit()
	else:
		print 'Not a valid Sudoku'

	
	# print nCheck
	# print new_ID
	# print_node(known_values_head)
	# print_node(known_values_head)
	
if __name__ == "__main__":
	main()
