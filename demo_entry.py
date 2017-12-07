#! /usr/bin/env/ python3

#can't use grid and pack in same prog
#tutorialspoint is the site to use.
#make scale with resizing
#new bottom line
#do it the ugly way first


from tkinter import *
import random

master = Tk()

e = Entry(master)
e.grid(row=0,column=0)
e.focus_set()
e2 = Entry(master)
e2.grid(row=4,column=0)

separator = Frame(master, height=15, bd=10, relief=SUNKEN)
separator.grid(row=7, column=0)

text = Text(master, bd=8,height=15)
text.grid(row=9,column=0)

def callback3():
    word = e.get()
    definition = e2.get()
    appendFile = open('words', 'a')#a meaning? #why use with
    appendFile.write('\n' + word + ': ' + definition)
    appendFile.close()
    
def review():
    #quiz by definition
    readFile = open('words', 'r') #be sure to close

    size = 0
    splitList = []
    for line in readFile:
        splitWord = line.split(':')
        splitWord = splitWord[1].strip('\n ')
        splitList.append(splitWord) #can condense this n line above?
        size += 1
        
    #size = sum(1 for line in readFile)
    n = random.randint(0, size - 1)
    text.insert(INSERT, splitList[n] + '\n')
 
    readFile.close()

def answer():
    
    
    
#________Buttons_______    
b = Button(master, text="word", width=10)
b.grid(row=1,column=0)
b2 = Button(master, text="commit", width=10, command=callback3)
b.grid(row=2,column=0)
b3 = Button(master, text="definition", width=10)
b3.grid(row=3,column=0)
b4 = Button(master, text="review", width=10, command = review)
b4.grid(row=8,column=0)
b5 = Button(master, text="show answer", width=10)#instead of master, lower frame?
b5.grid(row=8,column=1)



mainloop()

        #later need button for submission, testing, or show correct first
