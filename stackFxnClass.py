#! usr/bin/env python3
#attempt to make class to pass arguments to tkinter functions

import tkinter as tk
from tkinter import *

class Functionality:

    def __init__(self, master):#include frame here?
        self.master = master
        self.bC = Button(master, text = 'Commit', command = self.commit)
        self.bC.pack(side='left')
        self.bR = Button(master, text = 'Review', command = self.review)#how do I pass the relevant file?
        self.bR.pack(side='left')
        self.bA = Button(master, text = 'Answer', command = self.answer)
        self.bA.pack(side='left')
        self.bH = Button(master, text = 'Hint', command = self.hint)
        self.bH.pack(side='left')
#maybe incl the bind <Button-1> jazz
    
    def commit(self, file_in_use):#need event=None?
        word = e1.get()
        definition = e2.get()
        appendFile = open(file_in_use, 'a')
        appendFile.write('\n' + word + ': ' + definition)
        appendFile.close()
        e1.delete(0, 'end')
        e2.delete(0, 'end')
    
    def review(self, file_in_use):
        t1.delete('1.0', END)

        readFile = open(file_in_use, 'r') 
        size = 0
        splitList = []
        for line in readFile:
            splitWord = line.split(':')
            splitWord = splitWord[0].strip('\n ')
            splitList.append(splitWord)
            size += 1
        
            n = random.randint(0, size - 1)
            t1.insert(INSERT, splitList[n] + '\n')
            readFile.close()

    def answer(self, file_in_use):
        word = e3.get()
        def1 = t1.get('1.0','end-1c')
        def1 = def1.strip('\n')
        readFile = open(file_in_use, 'r') 
        for line in readFile:
            splitWord = line.split(': ')
            if def1 == splitWord[0].strip('\n'):
                if word == splitWord[1].strip('\n'):
                    t1.insert(INSERT, 'Good job!')
                else:
                    t1.insert(INSERT, 'Not quite! Good try =)')
        readFile.close()

    def hint(self, file_in_use):
        def1 = t1.get('1.0','2.0')
        def1 = def1.strip('\n')
        readFile = open(file_in_use, 'r')
    
        for line in readFile:
            splitWord = line.split(': ')
            if def1 == splitWord[0].strip('\n'):
                hint = splitWord[1]

        hint1 = t1.get('2.0','end-1c')
        lenHint1 = len(hint1)
        if lenHint1 >= len(hint):
            pass
        else:
            t1.insert(INSERT, hint[lenHint1])
            print (hint1)
        readFile.close()
