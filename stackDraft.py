#! usr/bin/env python3

#import tkinter as tk? 
from tkinter import *
import random
from stackClass import GUI
from stackFxnClass import Functionality


master = Tk() 

f0 = Frame(master)
f0.pack()

f1 = Frame(master)
f1.pack()
f2 = Frame(master)
f2.pack()
f3 = Frame(master)
f3.pack()
l1 = Label(f1, text='word:').pack(side='left')
l2 = Label(f2, text='definition:').pack(side='left')

e1 = Entry(f1)
e1.pack(side='right')
e2 = Entry(f2)
e2.pack(side='right')
t1 = Text(f3, height = 4, bg = 'lavender')
e3 = Entry(f3)

#____________Functions____________

file_switch__test = GUI(master)
fxns_test = Functionality(master)
file_in_use = 'farsi_words'

# def defaultFile(filename):
#     file_in_use = filename
#     return file_in_use

# bN = Button(f0, text = 'Nouns', command =lambda: defaultFile('farsi_words'))
# bN.pack(side='left')
# bV = Button(f0, text = 'Verbs', command =lambda: defaultFile('farsi_verbs'))
# bV.pack(side='left')
# bA = Button(f0, text = 'Adjectives', command =lambda: defaultFile('farsi_adj'))
# bA.pack(side='left')
# bP = Button(f0, text = 'Prepositions', command =lambda: defaultFile('farsi_preps'))
# bP.pack(side='left')




# def commit(file_in_use):
#     word = e1.get()
#     definition = e2.get()
#     appendFile = open(file_in_use, 'a')
#     appendFile.write('\n' + word + ': ' + definition)
#     appendFile.close()
#     e1.delete(0, 'end')
#     e2.delete(0, 'end')
    
# def review(file_in_use):
#     t1.delete('1.0', END)

#     readFile = open(file_in_use, 'r') 
#     size = 0
#     splitList = []
#     for line in readFile:
#         splitWord = line.split(':')
#         splitWord = splitWord[0].strip('\n ')
#         splitList.append(splitWord)
#         size += 1
        
#     n = random.randint(0, size - 1)
#     t1.insert(INSERT, splitList[n] + '\n')
#     readFile.close()

# def answer(file_in_use):
#     word = e3.get()
#     def1 = t1.get('1.0','end-1c')
#     def1 = def1.strip('\n')
#     readFile = open(file_in_use, 'r') 
#     for line in readFile:
#         splitWord = line.split(': ')
#         if def1 == splitWord[0].strip('\n'):
#             if word == splitWord[1].strip('\n'):
#                 t1.insert(INSERT, 'Good job!')
#             else:
#                 t1.insert(INSERT, 'Not quite! Good try =)')
#     readFile.close()

# def hint(file_in_use):
#     def1 = t1.get('1.0','2.0')
#     def1 = def1.strip('\n')
#     readFile = open(file_in_use, 'r')
    
#     for line in readFile:
#         splitWord = line.split(': ')
#         if def1 == splitWord[0].strip('\n'):
#             hint = splitWord[1]

#     hint1 = t1.get('2.0','end-1c')
#     lenHint1 = len(hint1)
#     if lenHint1 >= len(hint):
#         pass
#     else:
#         t1.insert(INSERT, hint[lenHint1])
#         print (hint1)
#     readFile.close()

# #____________Buttons____________
        
# b1 = Button(f3, text = 'commit', command = commit)
# b1.pack()
# b2 = Button(f3, text = 'review (press for new word)', command = review)
# b2.pack()
# b3 = Button(f3, text = 'answer', command = answer)
t1.pack()
# b4 = Button(f3, text = 'hint', command = hint)
e3.pack(side = 'right')
# b3.pack(side = 'right')
# b4.pack(side = 'right')
mainloop()
