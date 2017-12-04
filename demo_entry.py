#! /usr/bin/env/ python3

from tkinter import *
import pickle

master = Tk()

e = Entry(master)
e.pack()
e.focus_set()
text = Text(master)
#text.pack()

def callback():
    print (e.get())

def callback2():
    word1 = e.get()
    text.insert(INSERT, word1)
    text.pack(side = BOTTOM)
    
b = Button(master, text="get", width=10, command=callback)
b.pack()
bb = Button(master, text="show", width=10, command=callback2)
bb.pack()


mainloop()#how is mainloop here, above other code?
e = Entry(master, width=50)
e.pack()
text = e.get()
pickle.dump( text, open('save.p','wb'))#will this save on 'get' click?












#def makeentry(parent, caption, width=None, **options):
#    Label(parent, text=caption).pack(side=LEFT)
#    entry = Entry(parent, **options)
#    if width:
#        entry.config(width=width)
#    entry.pack(side=LEFT)
#    return entry

#user = makeentry(parent, "User name:", 10)
#password = makeentry(parent, "Password:", 10, show="*")
#content = StringVar()
#entry = Entry(parent, text=caption, textvariable=content)

#text = content.get()
#content.set(text)

#mainloop()
