# Tyler Geonetta
# Prints a random, valid sudoku board

import random

sudoku = [] # Initializing game board
sudokuLength = 81 # Game board size 9*9 Edited by Tim W #2014/12/19



def main():
	for i in range(sudokuLength):
		sudoku.append(None) # populate board with nulls
	populateCell(0)	
	printSudoku()

# Recursively populates sudoku board
def populateCell(box):
	if box == sudokuLength:
		return True		
	oneToNine = range(1,10)
	for i in range(9):
		sudoku[box] = random.choice(oneToNine)
		oneToNine.remove(sudoku[box])		
		if boxIsValid(sudoku[box], box):
			if populateCell(box+1):
				return True
	sudoku[box] = None
	return False
	
# Checks all 3 conditions for a valid sudoku		
def boxIsValid(num, box):
	if checkVertical(num, box) and checkHorizontal(num, box) and check3x3(num, box):
		return True
	else:
		return False

# Checks for a valid 3x3 square			
def check3x3(num, box):
	temp = box
	row = 0
	while temp >= 9:
		temp -= 9
		row += 1
	if row % 3 == 0:
		return True # Checking would be redundant
	else:
		temp = box
		offset = box % 3
		for i in range(row % 3): # range(1 or 2)
			temp -= 9
			for j in range(3):
					if num == sudoku[temp - offset + j]:
						return False
	return True

# Checks for a valid horizontal line	
def checkHorizontal(num, box):
	offset = box % 9
	for i in range(1, offset+1):
		if num == sudoku[box - i]:
			return False
	return True

# Checks for a valid vertical line
def checkVertical(num, box):
	box -= 9
	while box >= 0:
		if num == sudoku[box]:
			return False
		box -= 9
	return True

# Printing in human-readable format
def printSudoku():
	temp = []
	for i in range(9):
		temp.append([])
	boxCtr = 0
	rowCtr = 0
	while boxCtr < 81:
		for i in range(9):
			temp[rowCtr].append(sudoku[boxCtr])
			boxCtr += 1
		rowCtr += 1
	for row in temp:
		print row
		
def getTable():# edited by Tim W
	for i in range(sudokuLength):
		sudoku.append(None)
	populateCell(0)	
	return sudoku
	

	
if __name__ == "__main__":
	main()