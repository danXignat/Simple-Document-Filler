import customtkinter as ctk

from frontend.CalendarEntry import DateEntry
from config import COLORS, BOX_WIDTH
from typing import List, Optional, Callable, Dict

class Scene(ctk.CTkFrame):
    def __init__(self, parent, controller, data_container : Dict):
        super().__init__(parent, border_color=COLORS["green"], border_width=2)
        self.controller = controller
        self.entries = data_container

        self.text_font = ctk.CTkFont(size=14, weight="bold")
        
    def create_combo_box(self, label: str, values : List, side: Optional[str] = "top", pady: int = 5, padx: int = 5, command : Callable = None, parent = None, str_var =  None):
        state = "disabled" if len(values) == 0 else "normal"
        
        str_var = str_var if str_var else ctk.StringVar(value=label)
        parent = parent if parent else self 
        
        combo_box = ctk.CTkComboBox(
            parent,
            values=values,
            fg_color=COLORS["blue"],
            button_hover_color=COLORS["dark_blue"],
            dropdown_hover_color=COLORS["dark_green"],
            font = self.text_font,
            width=BOX_WIDTH,
            command=command,
            state = state,
            variable=str_var
        )
        
        combo_box.bind("<FocusIn>", lambda e: str_var.set("") if str_var.get() == label else None)
        combo_box.bind("<FocusOut>", lambda e: str_var.set(label) if str_var.get() == "" else None)
        
        combo_box.pack(side=side, pady=pady, padx=padx)
        
        return str_var, combo_box

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

    def create_entry(self, label: str, side: Optional[str] = "top", pady: int = 5, padx: int = 5, parent = None):
        str_var = ctk.StringVar(value=label)
        
        parent = parent if parent else self
        
        entry = ctk.CTkEntry(
            parent,
            textvariable=str_var,
            border_color=COLORS["blue"],
            placeholder_text_color=COLORS["light_blue"],
            font = self.text_font,
            width=BOX_WIDTH
        )
        entry.pack(side=side, pady=pady, padx=padx)
        
        entry.bind("<FocusIn>", lambda e: str_var.set("") if str_var.get() == label else None)
        entry.bind("<FocusOut>", lambda e: str_var.set(label) if str_var.get() == "" else None)
        
        return str_var

    def create_label(self, label: str, side: Optional[str] = "top", pady: int = 5, padx: int = 5):
        title_label = ctk.CTkLabel(
            self,
            text=label,
            text_color=COLORS["green"],
            font=COLORS["label_font"],
        )
        title_label.pack(side=side, pady=pady, padx=padx)
        
        return title_label

    def create_date(self, label):
        calendar = DateEntry(self, label, fg_color=self._fg_color)
        calendar.pack(pady=10)        

        return calendar.string_var
    
    def load_state(self, data_container: dict):
        for label, value in data_container.items():
            if label in self.entries:
                self.entries[label].delete(0, "end")
                self.entries[label].insert(0, value)
