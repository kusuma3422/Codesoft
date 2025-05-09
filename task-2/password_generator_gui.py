import tkinter as tk
from tkinter import messagebox
import random
import string

# Password generation function
def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            raise ValueError("Length too short")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password:\n{password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid length (min 4).")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11), wraplength=300)
result_label.pack(pady=10)

# Start GUI loop
root.mainloop()
