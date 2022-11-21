import tkinter as tk
from tkinter import ttk
from tkinter_input_box import InputBox

root = tk.Tk()
root.geometry("600x600")

# create input box
inp_normal = InputBox(root)
inp_normal.pack()

# input box with default text
InputBox(root, text="hello world").pack()

# input box with default text and placeholder
InputBox(root, text="hello world", placeholder="placeholder").pack()

# input box with placeholder
inp_box = InputBox(root, placeholder="input box", font=("", 25))
inp_box.pack()

# input box with font color and placeholder color



root.mainloop()