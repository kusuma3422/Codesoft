import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid operation"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Dropdown for operations
tk.Label(root, text="Select operation:").pack(pady=5)
operation = tk.StringVar()
operation.set("+")  # default value
operations_menu = tk.OptionMenu(root, operation, "+", "-", "*", "/")
operations_menu.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
