## Preamble
"""
# Program: TkinterTestFile.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Sep  9 15:25:41 2021
# Date Modified: Thu Sep  9 15:25:41 2021
# Purpose: Test the tkinter GUI framework for processing interface for HTC.
# Imports: tkinter
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles
import tkinter as tk
window = tk.Tk()
button  = tk.Button(window,text="STOP",width=25,command=window.destroy)
button.pack()
window.mainloop()


# M02 End Program