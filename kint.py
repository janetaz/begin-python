#!/usr/bin/env python3
#thenewboston's python class tutorials, then Tkinter 8

#______
from tkinter import *
root = Tk() 
#______

verb_dict = {}
noun_dict = {}

text = Text(root)
entry1 = Entry(root)


def showDef():
    text.insert(INSERT, "Word here.")
    text.pack()

def addWord():
    entry1.pack(side = BOTTOM)
    newWord = entry1.get()
    text.insert(INSERT, newWord)
    text.pack(side = BOTTOM)
    return verbList

#def newWord(word, definition):
    #global dictionary, OR write to file. maybe OH save to two files: verbs, nouns, parts of speech. but you just add..."word: definition here" then split on a colon to withdraw

def newWord():
    entry1.pack(side = BOTTOM)
    word1 = entry1.get()
    appendFile = open('store', 'a')#need .txt?
    appendFile.write('\n' + word1)
    appendFile.close()
    #open file, write to IN ADDITION

topFrame = Frame(root)
topFrame.pack()#defaults to top
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Review", command = showDef)#no parens
button2 = Button(topFrame, text="New word", command = newWord)
#command = addWord)
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)


#______
root.mainloop() 
#______
