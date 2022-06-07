import tkinter as tk
import sys

class ConsoleOutput(): 
    def __init__(self, textbox): 
        self.textbox = textbox

    def write(self, text):

        # Inserts text into the console textbox
        self.textbox.insert(tk.END, text)
        self.textbox.see('end')
            # could also scroll to end of textbox here to make sure always visible

    # Necessary for use
    def flush(self): 
        pass
