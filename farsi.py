#! usr/bin/env python3
#update in real time
#english and farsi
#clear answer box each time press review
#hint button; one letter at a time
#using dictionary API

#to switch from English to Farsi: define 'words' or 'farsi_words' as a generic variable that u feed to the functions. have everything couched in an 'if' statement? or, just have two buttons that switch the main one
#can simluate switchin' pages using frames. can i nest frames? i will figure out my frame sitch.

#ok, hint function
#is there a way I can feed variables to these functions, so I don't have to reopen file each time?

from tkinter import *
import random

master = Tk() 

f1 = Frame(master)#(master).pack() doesn't work
f1.pack(side="top")
f2 = Frame(master)
f2.pack()#side="bottom")
f3 = Frame(master)
f3.pack(side="bottom")
l1 = Label(f1, text='word:').pack(side='left')
l2 = Label(f2, text='definition:').pack(side='left')

e1 = Entry(f1)
e1.pack(side='right')
e2 = Entry(f2)
e2.pack(side='right')
t1 = Text(f3, height = 4, bg = 'lavender')#EA7258)
e3 = Entry(f3)

#____________Functions____________

def commit():
    word = e1.get()
    definition = e2.get()
    appendFile = open('farsi_words', 'a')
    appendFile.write('\n' + word + ': ' + definition)
    appendFile.close()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    
def review():
    t1.delete('1.0', END) #replaces
    #t1.pack()
    #e3.pack(side = 'right')
    #b3.pack(side = 'right')

    readFile = open('farsi_words', 'r') 
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

def answer():
    word = e3.get()
    def1 = t1.get('1.0','end-1c')#cuts off newline, but didn't work. needed split
    def1 = def1.strip('\n')
    readFile = open('farsi_words', 'r') 
    for line in readFile:
        splitWord = line.split(': ')
        if def1 == splitWord[0].strip('\n'):
            if word == splitWord[1].strip('\n'):
                t1.insert(INSERT, 'Good job!')
            else:
                t1.insert(INSERT, 'Not quite! Good try =)')
    readFile.close()

def hint():
    def1 = t1.get('1.0','end-1c')
    def1 = def1.strip('\n')
    readFile = open('farsi_words', 'r') 
    for line in readFile:
        splitWord = line.split(': ')
        if def1 == splitWord[0].strip('\n'):
            hint = splitWord[1]

    count = 0
    t1.insert(INSERT, hint[count])
    count += 1
    #hint referenced before assignment...when I call hint() more than once
    readFile.close()

#____________Buttons____________
        
b1 = Button(f3, text = 'commit', command = commit)
b1.pack()
b2 = Button(f3, text = 'review (press for new word)', command = review)
b2.pack()
b3 = Button(f3, text = 'answer', command = answer)
t1.pack()
b4 = Button(f3, text = 'hint', command = hint)
e3.pack(side = 'right')
b3.pack(side = 'right')
b4.pack(side = 'right')
mainloop()
