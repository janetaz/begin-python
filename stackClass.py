#! usr/bin/env python3

import tkinter as tk
from tkinter import *


class GUI:

    def __init__(self, master):
        self.file_in_use = 'farsi_words'
        self.master = master
        self.bN = Button(master, text = 'Nouns', command = self.farsi_words)
        self.bN.pack(side='left')
        self.bN.bind("<Button-1>")#what does bind do?
        self.bV = Button(master, text = 'Verbs', command = self.farsi_verbs)
        self.bV.pack(side='left')
        self.bA = Button(master, text = 'Adjectives', command = self.farsi_adjectives)
        self.bA.pack(side='left')
        self.bP = Button(master, text = 'Prepositions', command = self.farsi_preps)
        self.bP.pack(side='left')

    def farsi_words(self, event=None):
        self.file_in_use = 'Nouns'
        self.master.after(1, self.commit)
  
    def farsi_verbs(self, event=None):
        self.file_in_use = 'Verbs'
        self.master.after(1, self.commit)

    def farsi_adjectives(self, event=None):
        self.file_in_use = 'Adjectives'
        self.master.after(1, self.commit)

    def farsi_preps(self, event=None):
        self.file_in_use = 'Prepositions'
        self.master.after(1, self.commit)

    def commit(self, event=None):
        print(self.file_in_use)

#if __name__ == "__main__":
#    root = Tk()
#    my_gui = GUI(root)
#    root.mainloop()
