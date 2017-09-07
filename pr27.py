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
#
#read up on functions from previous project, all those links
#_____________________________

#from pr24 import writeTop, writeVert, writeBoard

#___printable board___
#board = writeBoard(5)
#print (board)

#___input getting function___
def turn(board):
    silo = [] #stores guess to be divided into ints
#Player 1 
    while True:
        move1 = (input("Player 1, choose a row & column: ")).split(',')
        for elem in move1:
            silo.append(elem.strip())#why does int not work?
        if board[int(silo[0]) - 1][int(silo[1]) - 1] != 0:#trying 0 vs '0'
            print ("Spot is occupied! Try again!")
        else:
            board[int(silo[0]) - 1][int(silo[1]) - 1] = 'x'
            break
#Player 2
#ohhh i was *appending* to silo, not replacing 
    silo2 = []
    while True:
        move2 = (input("Player 2, choose a row & column: ")).split(',')
        for elem in move2:
            silo2.append(elem.strip())#why does int not work?
        if board[int(silo2[0]) - 1][int(silo2[1]) - 1] != 0:
            print ("Spot is occupied! Try again!")
        else:
            board[int(silo2[0]) - 1][int(silo2[1]) - 1] = 'o'
            break

#simpler way to do ^ == generalized 1 turn function, taking player number, board, and x/o but, I'd need to pass the board from the previous fnxn

    #board will need to be updated, returned, then recycled
    boardNew = board
    return boardNew


    #indent whole stuff:
if __name__ == '__main__':

    #___game board (internal use)___
    staticBoard = [[0,0,0],
             [0,0,0],
             [0,0,0]] #cute pythonic way to do this?

    print ("Welcome to the game! Press Control + C to quit.")
    #while True:
    round1 = turn(staticBoard)
    for lis in round1:
        print (lis)



