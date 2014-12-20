#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__='Tim W'

import typlerGen, random # use the Tyler's generator

#sudoku game class
class sudokuGame(object):
	#init
	def __init__(self,difficulty,table):
		self.num=difficulty
		self.game=table
		
	#return a list as sudoku game
	def getSudokuGame(self):
		for i in range(0,self.num):
			tmp=random.randint(0,80)## ? can not keep the space is num  so improve it
			self.game[tmp]=0
		return self.game
	
	#out put the sudoku game list for human reading	
	def printSudoku(self):
		tmpGame=self.getSudokuGame()
		temp = []
		for i in range(9):
			temp.append([])
		boxCtr = 0
		rowCtr = 0
		while boxCtr < 81:
			for i in range(9):
				temp[rowCtr].append(tmpGame[boxCtr])
				boxCtr += 1
			rowCtr += 1
		for row in temp:
			print row

def main():
	
	#randomly choose the game difficulty
	difficulty=random.randint(65,75)
	
	#crete an instance of the sudoku game class
	gameA=sudokuGame(difficulty,tylerGen.getTable())

	#print(gameA.getSudokuGame())
	gameA.printSudoku()
	return 0

if __name__ == '__main__':
	main()