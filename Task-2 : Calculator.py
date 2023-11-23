import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place entry widget
entry = tk.Entry(root, width=20, font=('Helvetica', 16), borderwidth=5, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Define buttons (without the period)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '+', '='
]

# Create and place buttons
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
tk.Button(root, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=3, pady=5)

# Assign the 'calculate' function to the '=' button
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=row_val, column=2, pady=5)

# Configure row and column weights
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
