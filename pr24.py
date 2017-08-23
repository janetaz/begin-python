#!usr/bin/env python3
#
#Goal: make tic tac toe board
#Need: get input for size, draw apropos size
#do by drawing one, then repeating? or by drawing indiv horiz bars, vert bars?
#I think the latter, bc there's some overlap in the verts that'd be hard
#
#
#hm...return swapped in for print in writeTop, Vert, allowed me to reuse specific instance calls. it appeats if i just print and not return, i can only use the variable defined instance once. compare to http://www.practicepython.org/solution/2015/11/01/24-draw-a-game-board-solutions.html
#
#____________________________


#_____Gets board size from user_____
def getSize():
    while True:
        try:
            size = int(input("Enter a size: "))
            break #ok, it's not about break...good prob solving
        except ValueError:
            print ('Try again!')
    return size

#_____creates horizontal_____
#For dimension = dims, board is dims across, dims +1 rows
def writeTop(dims):
    return (' ---' * dims)# hmm... return 

#_____Creates vertical_____
#for dimension = dims, prints dims +1 across, no space before/after
def writeVert(dims):
    return ('|   ' * (dims + 1))

#___programs take care of the horizontal: this takes care of the vert___

if __name__ == '__main__':
    tes = getSize()
    horizontal = writeTop(tes)
    vertical = writeVert(tes)
    for x in range(tes):
        print (horizontal)
        print (vertical)
    print (horizontal)
