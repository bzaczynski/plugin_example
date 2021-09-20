"""
A plugin that displays a message box using Tkinter.
"""

import tkinter
from tkinter import messagebox


def main(text, title="Alert"):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
