import tkinter as tk
from tkinter import messagebox

def confirm_action():
    result = messagebox.askyesno("Confirmation", "Are you sure?")
    if result:
        print("Action confirmed!")
    else:
        print("Action canceled!")

# Create the main application window
root = tk.Tk()
root.title("Are You Sure Example")

# Add a button to trigger the confirmation dialog
button = tk.Button(root, text="Perform Action", command=confirm_action)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
