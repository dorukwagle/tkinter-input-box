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
in_box1 = InputBox(root, placeholder="test placeolder", placeholder_color="green", font_color="#ff00ff", font=("", 25))
in_box1.pack()

# password input box
inp_pass = InputBox(root, placeholder="enter password", placeholder_color="grey", input_type="password", font=("", 25))
inp_pass.pack()

# password input box with show option
inp_pass1 = InputBox(root, placeholder="enter password", placeholder_color="grey", input_type="password",
                    show="&", font=("", 25))
inp_pass1.pack()

root.mainloop()
