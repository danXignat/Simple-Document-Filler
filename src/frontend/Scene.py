from pydoc import text
from tkinter import font
import customtkinter as ctk
from config import COLORS
from typing import List, Optional, Callable

class Scene(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, border_color=COLORS["green"], border_width=2)
        self.controller = controller
        self.entries = {}

        self.text_font = ctk.CTkFont(size=14, weight="bold")
        
    def create_combo_box(self, label: str, values : List, side: Optional[str] = "top", pady: int = 5, padx: int = 5, command : Callable = None):
        state = "disabled" if len(values) == 0 else "normal"
        
        combo_box = ctk.CTkComboBox(
            self,
            values=values,
            fg_color=COLORS["blue"],
            button_hover_color=COLORS["dark_blue"],
            dropdown_hover_color=COLORS["dark_green"],
            font = self.text_font,
            width=300,
            command=command,
            state = state
        )
        combo_box.set(label)
        combo_box.pack(side=side, pady=pady, padx=padx)
        
        return combo_box

    def create_button(self, label: str, command: Callable, side: Optional[str] = "top", pady: int = 10, padx: int = 5, parent = None):
        parent = self if parent == None else parent
        
        button = ctk.CTkButton(
            master = parent,
            text=label,
            command=command,
            fg_color=COLORS["green"],
            hover_color=COLORS["dark_green"],
            font = self.text_font
        )
        button.pack(pady=pady, padx=padx, side = side)
        
        return button

    def create_entry(self, label: str, side: Optional[str] = "top", pady: int = 5, padx: int = 5):
        entry = ctk.CTkEntry(
            self,
            placeholder_text=label,
            border_color=COLORS["blue"],
            placeholder_text_color=COLORS["light_blue"],
            font = self.text_font,
            width=300
        )
        entry.pack(side=side, pady=pady, padx=padx)
        
        self.entries[label] = entry
        
        return entry

    def create_label(self, label: str, side: Optional[str] = "top", pady: int = 5, padx: int = 5):
        title_label = ctk.CTkLabel(
            self,
            text=label,
            text_color=COLORS["green"],
            font=COLORS["label_font"],
        )
        title_label.pack(side=side, pady=pady, padx=padx)
        
        return title_label

    def load_state(self, data_container: dict):
        for label, value in data_container.items():
            if label in self.entries:
                self.entries[label].delete(0, "end")
                self.entries[label].insert(0, value)
