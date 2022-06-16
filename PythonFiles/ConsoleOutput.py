# Importing all the necessary modules
import tkinter as tk
import sys

# Creates a class to be instantiated for writing, needs the entry box it is writing into passed in
class ConsoleOutput(): 
    def __init__(self, entry): 
        self.entry = entry

    # The write command adds the text into the entry box 
    def write(self, string):

        # Inserts text into the console entry box
        self.entry.insert(tk.END, string)
        self.entry.see('end') # Scrolls to the bottom of the text in the entry box

    # Necessary for use
    def flush(self): 
        pass