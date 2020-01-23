'''
01/23/2020
Advaith Nair
Mockify App
Description: Essentially formats inputted text into Mocking Spongebob so my shift key won't suffer :)
'''

import random
from tkinter import *

# Formats Mocked Text
def return_mocking():
    # Input Text Retrived from Text Entry (Top)
    inputText = textEntry.get()
    newList = list(inputText.lower())

    # String (Converted to List) Iteration by Character
    for i in range(len(newList)):
        if newList[i] == 'i':
            newList[i] = 'i' # I want 'i's to be lowercase
        elif newList[i] == 'l':
            newList[i] = 'L' # I want 'L's to be uppercase
        else:
            # Randomized upper/lower case
            if bool(random.getrandbits(1)):
                newList[i] = newList[i].upper()
            else:
                newList[i] = newList[i].lower()

    # Inserts Mocked Text into Text Box (Bottom)
    clear_text()
    outputText.insert(INSERT, "".join(newList))

def clear_entry():
    # Deletes Current Text in Text Entry (Top)
    textEntry.delete(0, 'end')

def clear_text():
    # Deletes Current Text in Text Box (Bottom)
    outputText.delete(1.0, END)

# Initialize GUI Window
window = Tk()
window.title("Mocking Text")
window.geometry("720x480")

# Initialize Text Entry (Top)
Label(window, text="Enter Text To Mock").pack()
textEntry = Entry(window, width=40, bg="white")
textEntry.pack()

# Initialize Buttons (Middle)
Button(window, text="Mockify", command = return_mocking).pack(ipadx = 5, ipady = 5)
Button(window, text="Clear Entry", command = clear_entry).pack(pady = 5, ipadx = 5, ipady = 5)
Button(window, text="Clear Text", command = clear_text).pack(pady = 5, ipadx = 5, ipady = 5)
Button(window, text="Quit", command = window.destroy).pack(pady = 5, ipadx = 5, ipady = 5)

# Initialize Text Box (Bottom)
outputText = Text(window, width = 60, height = 15, highlightbackground = "black", insertborderwidth = 5)
outputText.pack()

# Runs Window After Initialization
window.mainloop()