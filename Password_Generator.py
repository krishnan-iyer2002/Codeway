import random
import string
from tkinter import *
import pyperclip

def generate_random_password():
    password_length = pass_length.get()
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    output_password.set(password)

def copy_to_clipboard():
    pyperclip.copy(output_password.get())

# Initialize Window
root = Tk()
root.geometry("400x400")
root.title("Password Generator App")

# Variables
output_password = StringVar()
pass_length = IntVar()

# Label and Spinbox for password length
Label(root, text='Password Length', font='Arial 12 bold').pack(pady=10)
Spinbox(root, from_=4, to_=32, textvariable=pass_length, width=24, font='Arial 16').pack()

# Generate password button
Button(root, text="Generate Password", command=generate_random_password, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

# Label and Entry for generated password
Label(root, text='Random Generated Password', font='Arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output_password, width=24, font='Arial 16').pack()

# Copy to clipboard button
Button(root, text='Copy to Clipboard', command=copy_to_clipboard, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()
