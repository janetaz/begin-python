#!usr/bin/env python3
#
#P1 = x, P2 = o
#row, column
#strip whitespace, so 1,2 = 1, 2
#invalid syntax on line x usually means i missed a close parens on line x - 1
#
#it would be useful to ahve a reverse index python thing. for elem in sinp1, inp1[elem's spot] = different thing
#
#Need: condition only accepting 1, 2, 3 as inputs
#Need: win condition that stops the game
#Need: condition that prevents overwriting of x, o
#_____________________________

from pr24 import writeTop, writeVert, writeBoard

#___printable board___
#board = writeBoard(5)
#print (board)

#___game board (internal use)___
board = [[0,0,0],
         [0,0,0],
         [0,0,0]] #cute pythonic way to do this?

print ("Welcome to the game! Press Control + C to quit.")
while True:
    inp1clean = []
    inp2clean = []

    inp1 = (input("Player 1, choose a row & column: ")).split(',')
    for elem in inp1:
        inp1clean.append(elem.strip())#why does int not work?
    board[int(inp1clean[0]) - 1][int(inp1clean[1]) - 1] = 'x'

    inp2 = (input("Player 2, choose a row & column: ")).split(',')
    for elem in inp2:
        inp2clean.append(elem.strip())
    board[int(inp2clean[0]) - 1][int(inp2clean[1]) - 1] = 'o'
#___Print board___
    for lis in board:
        print (lis)
    
