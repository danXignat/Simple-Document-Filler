import customtkinter as ctk
from typing import Callable, Optional

from config import COLORS

class BackNext(ctk.CTkFrame):
    def __init__(self, master, back_func : Callable, next_func : Callable, fg_color, back_label: Optional[str] = "Inapoi", next_label: Optional[str] = "Urmatorul"):
        super().__init__(master, fg_color=fg_color, height=50)
        
        self.pack_propagate(False)
        self.pack(padx = 5, pady = 5, side = "bottom", fill = "x")
        
        self.text_font = text_font = ctk.CTkFont(size=14, weight="bold")    
        
        self.back = self.create_button(back_label, 0, "left", back_func)
        self.next = self.create_button(next_label, 1, "right", next_func)
        
    def create_button(self, label: str, column : int, side : str, command : Callable) :
        button = ctk.CTkButton(
            master=self,
            text=label,
            command=command,
            fg_color=COLORS["green"],
            hover_color=COLORS["dark_green"],
            font=self.text_font
        )
        button.pack(padx=10, pady=10, side = side)
        
        return button