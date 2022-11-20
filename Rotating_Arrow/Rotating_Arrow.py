'''Arrows'''
import os
from time import sleep
##Whole screen for rotation : consists of 2 * 18 width & length
##One arrow consists of : 18 width & 18 length 
coloumns = 14
rows = 14
while 1:
	'''Pointing Right'''
	for i in range (1,2*rows):
			for j in range (1,2*coloumns):
				if (j<coloumns or i<=rows/2 or i>=3*rows/2): #Borders of the drawing
					print(" ",end=" ")
				elif ((i<rows) and (j<3*coloumns/2)): #up to Middle line
					print(" ",end=" ")
				elif((i>rows) and (j<3*coloumns/2)): #down to Middle line
					print(" ",end=" ")
				elif(i<=(j-rows) or i>=(-j+3*rows)): #Function of straight line (the pointing lines)
					print(" ",end=" ")
				else:
					print("*",end=" ")
			print("\n",end="")
	print("\n",end="")	
	sleep(1)
	os.system('cls')
	'''Pointing Down'''
	for i in range (1,2*rows):
			for j in range (1,2*coloumns):
				if (i<rows or j<=coloumns/2 or j>=3*coloumns/2): #Borders of the drawing
					print(" ",end=" ")
				elif ((i<3*rows/2) and (j<coloumns)):#left to Middle line
					print(" ",end=" ")
				elif((i<3*rows/2) and (j>coloumns)): #right to Middle line
					print(" ",end=" ")
				elif(i>=(j+rows) or i>=(-j+3*rows)): #Function of straight line (the pointing lines)
					print(" ",end=" ")
				else:
					print("*",end=" ")
			print("\n",end="")
	print("\n",end="")
	sleep(1)
	os.system('cls')
	'''Pointing Left'''
	for i in range (1,2*rows):
			for j in range (1,2*coloumns):
				if (j>coloumns or i<=rows/2 or i>=3*rows/2): #Borders of the drawing
					print(" ",end=" ")
				elif ((i<rows) and (j>coloumns/2)): #up to Middle line
					print(" ",end=" ")
				elif((i>rows) and (j>coloumns/2)): #down to Middle line
					print(" ",end=" ")
				elif(i<=(-j+rows) or i>=(j+rows)): #Function of straight line (the pointing lines)
					print(" ",end=" ")
				else:
					print("*",end=" ")
			print("\n",end="")
	print("\n",end="")	
	sleep(1)
	os.system('cls')			
	'''Pointing Up'''
	for i in range (1,2*rows):
			for j in range (1,2*coloumns):
				if (i>rows or j<=coloumns/2 or j>=3*coloumns/2): #Borders of the drawing
					print(" ",end=" ")
				elif ((i>rows/2)and (j<coloumns)): #left to Middle line
					print(" ",end=" ")
				elif((i>rows/2)and (j>coloumns)): #right to Middle line
					print(" ",end=" ")
				elif(i<=(-j+rows) or i<=(j-rows)): #Function of straight line (the pointing lines)
					print(" ",end=" ")
				else:
					print("*",end=" ")
			print("\n",end="")
	print("\n",end="")
	sleep(1)
	os.system('cls')

