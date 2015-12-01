"""
sudokuToSAT
University of Victoria
Computer Science 320, Fall 2015
Kyle Hoffmann - V00812422
// Note to group: Add your names here!
"""

import os
import sys
import math
from sys import exit, argv

#####
# Node that stores the id of a character in the puzzle. (Currently accepts everything but '0', '.', '?', and '*')
#	Saves the character and the id associated with it. Needs to know it's own ID.
#####
class ID_Node:
	def __init__(self, character=None, id=None, next=None):
		self.character = character
		self.id = id
		self.next  = next

#####
# Node that a solved entry in the puzzle, it keeps the id of the character known, and the location in the puzzle (indexed at 0).
#	Saves the character's ID and the locaton of the character.
#####
class Entry_Node:
	def __init__(self, location=None, id=None, next=None):
		self.location = location
		self.id = id
		self.next  = next

#####
# Checks the known characters in the puzzle, if the character being processed already has an ID, it's Id is returned otherwise -1 is returned.
#####
def get_character_ID( head, character ):
	node = head
	# Accounts for the list of known Characters being empty.
	if head == -1:
		return -1

	# Loop through list of character IDs.
	while node:
		if node.character == character:
			return node.id
		node = node.next

	# Character does not have an ID.
	return -1

#####
# Adds a new character to the end of the known characters list.
#####
def new_character_ID( tail, id, character ):
	# Makes an entry for the known character list.
	node = ID_Node(character, id)
	# Detects if the list of known characters is empty.
	if tail != -1:
		# Appends the new character to the end of the list. (Dosent update pointer to the end of the list though.)
		tail.next = node
	# Returns a link to the new character entry.
	return node

#####
# Used to reverse the characters from the known character list to their original character in the unsolved sudoku.
#	It reads through the known character list and uses the id of the character to find the true value of the 
#	character and returns it.
#	It is only implemented for integers as it is inteded to be used to fix the 9x9 case where the characters are 1-9.
#	Functional, not optimal. A better implementation remake this list and use an array with the corrected values.
#####
def get_fix_character_ID( head, id ):
	node = head

	# Watches for an empty list of characters to avoid addressing issues.
	if head == -1:
		return -1

	# Loops though the list of known characters
	while node:
		# Finds the correct ID
		if node.id == id:
			# Makes sure the value found is an integer and returns it
			try:
				return int(node.character)
			except ValueError:
				print 'fatal error, id given is not connected to an integer value'
				return -1
		# Moves forward in the known character list.
		node = node.next
	return -1

#####
# Used to reverse the characters from the known character list to their original character in the unsolved sudoku.
#	Loops though the known puzzle entries and corrects their ID to the original value the puzzle gave them.
#	It is only implemented for integers as it is inteded to be used to fix the 9x9 case where the characters are 1-9.
#####
def fix_character_ID( puzzle_head, id_head ):
	node = puzzle_head
	# Fixes every entry in the known puzzle entry list.
	while node:
		# Calls a function to correct the id of the current entry.
		node.id = get_fix_character_ID( id_head, node.id )
		# Moves to the next entry.
		node = node.next

#####
# Used for testing. Prints off details of either the known puzzle entry, or known character list.
#	print statments must manually be commented out for this to work. Some statments will cause errors
#	for the list that dosent have the attribute connected to it.
#####
def print_node(head):
	node = head
	while node:
		# print node.location
		print node.id
		# print node.character
		node = node.next

#####
# Writes the minimal Encoding. 
#	See assigment document for details. (Note: instead of converting from base 9, it was just indexed at 0).
#	Works for the NxN case. 
#####
def write_mimimal_miniSat_encoding( puzzle_head, size ):
	# Attempts to write the encoding to a reserved file. 
	try:
		meta_file = open('miniSat_readypuzzle', 'w')
	except IOError:
		print("Error in opening " + 'miniSat_readypuzzle')
		print("Verify the file exists and/or the correct permissions are set for this file.")
		exit()

#####
# Checks the validity of the puzzle, and the user's useage of the program.
#	Program has a special case for the 9x9 puzzle where all characters are 1-9. This allows the solved puzzle reader to 
#	differentiate from a standard puzzle and a special case puzzle so the markers can feed generic solved puzzles into it
#	without a .meta file.
#####
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

	# Verify we have a puzzle to solve
	if len(argv) < 2:
		print("Usage of program: 'py miniSAT.py <puzzle>'")
		print("<puzzle> can be an in-line puzzle from the command line, or the name of a file containing a puzzle.")
		exit()

	if os.path.exists(argv[1]):
		try:
			puzzle = open(argv[1], 'r')
			# Loop through all the lines of the puzzle, read each individual character
			# If the character is not a newline or a blank space and is in the known character list, its ID is found, and its 
			# location is added to the known puzzle entry list, and it is counted. If the character is one of '0', '.', '?', 
			# and '*' it is counted as an empty character. Otherwise it is a new chracter and is added to the known character 
			# list, then the program follows the logic for a known valid character.
			# if it is a space or newline it is not counted.
			# This continues until the EOF is found.
			# Once all the entries have been counted it checks if its fourth root is a natural number (excluding 0). If so 
			# it is valid puzzle. 
			while True:
				# read the next character.
				c = puzzle.read(1)
				# break if character can't be read or we're at EOF
				if not c:
					break
				else:
					cInt = c
					# Catch integer entries. (needed for the 9x9 1-9 character case.)
					try:
						if 1 <= int(cInt) <= 9:
							# A character in the puzzle was found, thus the total number of characters found has increased
							charactersScanned += 1
							# Get id
							current_ID = get_character_ID( head, c )
							# Catches the case that the current character is a new
							# character.
							if current_ID == -1:
								# Adds new character to the known character list.
								node = new_character_ID(tail, new_ID, c)
								# Remembers the id of the new character so the current entry can be added to 
								# the known puzzle entry list.
								current_ID = new_ID
								# Insures each character has a unique ID.
								new_ID += 1
								# Makes the tail of the list point to the newest character.
								tail = node
								# Checks if the known character list was empty.
								if head == -1:
									# Given there was no known character list, it makes the new character 
									# the first character.
									head = node
								# Keeps track of the values between 1-9 present in the puzzle for the 
								# 9x9 1-9 character case.
								ints_found += 1
							# Adds the currently found puzzle solution to the known puzzle entry list.
							node = Entry_Node(charactersScanned, current_ID)
							# Catches if the known puzzle entry list was empty.
							if known_values_head == -1:
								# Given there was no known puzzle entry list, it makes the new puzzle entry 
								# the first puzzle entry.
								known_values_head = node
							else:
								# Given there was a known puzzle entry list the new entry is added to the 
								# end of the list
								known_values_tail.next = node
							# The last known puzzle entry is updated to the current one.
							known_values_tail = node
							# The number of unique characters in the sudoku is tracked. If it exceeds the n 
							# (from nxn) the puzzle is invalid.
							number_of_known_values += 1


						else:
							# If the character scanned is a 0, it is a unknown in the puzzle and is treated as such.
							# Specifically the total scanned characters is increased by one.
							charactersScanned+=1


					except ValueError:
						# If the current symbol is a unknown in the puzzle it is treated as a '0'
						# Specifically the total scanned characters is increased by one.
						if c == "." or c == "?" or c == "*":
							charactersScanned += 1
						# If the current character is a spaceing character it is skipped without adding to the total
						# of scanned characters.
						elif ( c =="\n" or c =="\s" or c =="\r" or c == "\t" ):
							pass
						else:
							# A character in the puzzle was found, thus the total number of characters found has increased
							charactersScanned += 1
							# Get id
							current_ID = get_character_ID( head, c )
							# Catches the case that the current character is a new
							# character.
							if current_ID == -1:
								# Adds new character to the known character list.
								node = new_character_ID(tail, new_ID, c)
								# Remembers the id of the new character so the current entry can be added to 
								# the known puzzle entry list.
								current_ID = new_ID
								# Insures each character has a unique ID.
								new_ID += 1
								# Makes the tail of the list point to the newest character.
								tail = node
								# Checks if the known character list was empty.
								if head == -1:
									# Given there was no known character list, it makes the new character 
									# the first character.
									head = node
							# Adds the currently found puzzle solution to the known puzzle entry list.
							node = Entry_Node(charactersScanned, current_ID)
							# Catches if the known puzzle entry list was empty.
							if known_values_head == -1:
								# Given there was no known puzzle entry list, it makes the new puzzle entry 
								# the first puzzle entry.
								known_values_head = node
							else:
								# Given there was a known puzzle entry list the new entry is added to the 
								# end of the list
								known_values_tail.next = node
							# The last known puzzle entry is updated to the current one.
							known_values_tail = node
							# The number of unique characters in the sudoku is tracked. If it exceeds the n 
							# (from nxn) the puzzle is invalid.
							number_of_known_values += 1

		except IOError:
			# Puzzle could not be opened, inform the user and end the program.
			print("Error in opening " + argv[1])
			print("Verify the file exists and/or the correct permissions are set for this file.")
			exit()
	else:
		# Puzzle DNE, print error.
		print("Error in opening " + argv[1])
		print("Verify the file exists and/or the correct permissions are set for this file.")
		exit()

	# Checks if the number of characters has a fourth root that is a natural number (excluding 0).
	# If the number has a fourth root it is a NxN puzzle where N is the square root of the total characters
	# in the puzzle. It must be a fourth root because every puzzle is a grid of KxK grids of KxK entries in 
	# each subgrid where K^2 = N for the subgrid trait of the sudoku to be a valid constraint. Otherwise 
	# Sudoku logic dosen't apply to the problem.

	# Gets the fourth root of the entries of th sudoku puzzle.
	nCheck = math.pow( (charactersScanned), 1.0/4)

	# Checks for the special case of a 9x9 puzzle with 1-9 being the characters used in the puzzle.
	# This allows simple testing for the second half of the program for any solved puzzles of this style
	# It is worth noting that if the meta file is deleted or faulty the second half will assume that the 
	# puzzle is of this format and will return a solved puzzle using 1-9 as entries.
	if nCheck*nCheck == 9 and ints_found == 9:
		# Reads through the known puzzle values and corrects the value stored in ID, so that the ID will be 
		# the literal value the puzzle was originally written in.
		fix_character_ID(known_values_head, head)
		# Tells program it can skip writing a metafile.
		skip_meta = True

	# Checks if the number of characters has a fourth root that is a natural number (excluding 0).
	# If so the puzzle is valid, proceed with encoding.
	# If not print error message.
	if (nCheck).is_integer() and math.pow( (nCheck), 4 ) == charactersScanned and (nCheck*nCheck + 1) >= new_ID:
		print 'Valid Puzzle'
		# Try to make meta file. If not possible program breaks.
		try:
			meta_file = open('sudoku.meta', 'w')
			# Considers that writing the meta could be skipped.
			if skip_meta == True:
				# Writes a value to the meta for the solution printer to know not to bother reading the file.
				meta_file.write( 'Skip Meta')
			else:
				# Given a meta is nessary the characters in the known chracter list is saved in the file at their
				# ID position.
				node = head
				while node:
					# saves the character value and gives it space for parsing.
					meta_file.write( node.character )
					meta_file.write( ' ' )
					# Moves to the next node for saving
					node = node.next
			# calls correct encoding fucntion.
			# write_mimimal_encoding(  )
		except IOError:
			print("Error in opening " + 'sudoku.meta')
			print("Verify the file exists and/or the correct permissions are set for this file.")
			exit()
	else:
		# Puzzle was not a valid sudoku, inform user and quit.
		print 'Not a valid Sudoku'

	
if __name__ == "__main__":
	main()
