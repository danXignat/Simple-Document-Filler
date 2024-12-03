import customtkinter as ctk
import tkinter as tk

class ScrollableComboBox(ctk.CTkFrame):
    def __init__(self, master, values, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create a CTkEntry for typing and a scrollbar
        self.entry = ctk.CTkEntry(self, placeholder_text="Search...")
        self.entry.pack(fill="both", padx=5, pady=5)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", padx=5, pady=5, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.frame = ctk.CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.values = values
        self.buttons = []
        self.create_buttons()

        self.frame.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))

    def create_buttons(self):
        """Creates buttons for each option"""
        for option in self.values:
            button = ctk.CTkButton(self.frame, text=option, width=200, command=lambda opt=option: self.select_option(opt))
            button.pack(pady=5)
            self.buttons.append(button)

    def select_option(self, option):
        """Handles selecting an option"""
        self.entry.set(option)

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create main window
root = ctk.CTk()
root.geometry("300x300")

# Create a list of options
options = [f"Option {i}" for i in range(1, 51)]  # 50 options

# Create and pack the ScrollableComboBox
scrollable_combobox = ScrollableComboBox(root, values=options)
scrollable_combobox.pack(pady=20, fill="both", expand=True)

root.mainloop()
