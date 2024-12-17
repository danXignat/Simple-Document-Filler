import customtkinter as ctk

from config import COLORS

class IDSCount(ctk.CTkFrame):
    def __init__(self, master, label: str):
        super().__init__(master=master, fg_color=COLORS["blue"])
        
        self.pack(padx = 5, pady = 5)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        count_label = ctk.CTkLabel(self, text = label, font=COLORS["text_font"])
        count_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        self.count_var = ctk.IntVar(value = 0)
        count = ctk.CTkLabel(self, textvariable = self.count_var, font=COLORS["text_font_bold"])
        count.grid(row = 0, column = 1, padx = 5, pady = 5)