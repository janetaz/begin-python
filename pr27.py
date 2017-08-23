#!usr/bin/env python3
#
#P1 = x, P2 = o
#row, column

#strip whitespace, so 1,2 = 1, 2

from pr24 import writeTop, writeVert, writeBoard #.py? ()?

#___printable board___
#board = writeBoard(5)
#print (board)

#___game board (internal use)___
board = [[0,0,0],
         [0,0,0],
         [0,0,0]] #cute way to do this?
while True:
    inp1 = input("Player 1, choose a row & column: ")
    inp1 = inp1.split(',')
    print (inp1)
    break
