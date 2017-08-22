#!usr/bin/env python3
#
#need to check columns, rows, diagonals, and can abandon if one is found to be true
#
#___test cases___
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
winner_by_rows = [[3, 3, 3],
	[2, 1, 0],
	[0, 1, 1]]

#rows: could clean, but I like the consistency

def win_lose(board): #takes list of lists called board
    l = len(board) - 1
    result = ''

    while l >= 0:
        if board[0][l] == board[1][l] == board[2][l]: #check columns
            result = str(board[l][0]) + '\'s win!'
        #l -= 1
        elif board[l][0] == board[l][1] == board[l][2]: #check rows
            result = str(board[l][0]) + '\'s win!'
        l -= 1
    return result
    #if board[0][0] == board[1][0] == board[2][0]:
        
            

a = win_lose(winner_by_rows)
print (a)
#OHHH! it starts at...never gets to 0. Yeahhhhh boyyy your boy figured it out. I'm dope. 
