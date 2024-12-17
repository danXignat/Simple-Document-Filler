from turtle import bgcolor
import customtkinter as ctk

from config import COLORS, BOX_WIDTH

class IDSFrame(ctk.CTkFrame):
    def __init__(self, master, data_container, fg_color, panel_count_var, height):
        super().__init__(master, fg_color = fg_color)
        self.panel_count_var = panel_count_var
        self.entries = data_container
        self.boxes = []
        
        self.text_font = ctk.CTkFont(size=14, weight="bold")
        
        self.entries_frame = ctk.CTkScrollableFrame(
            self,
            width=BOX_WIDTH,
            height=height,
            scrollbar_fg_color = "transparent",
            scrollbar_button_color = COLORS["green"],
            scrollbar_button_hover_color = COLORS["dark_green"]
            )
        
        self.entries_frame.grid_columnconfigure(0, weight=1)
        self.entries_frame.grid_columnconfigure(1, weight=1)
        
        self.entries_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        self.remove_button = ctk.CTkButton(self, text="Sterge serie", command=self.remove_entry, fg_color=COLORS["blue"], hover_color=COLORS["dark_blue"],font = self.text_font)
        self.remove_button.grid(row=1, column= 0, padx=5, pady=5)

        self.add_button = ctk.CTkButton(self, text="Adauga serie", command=self.add_entry, fg_color=COLORS["blue"], hover_color=COLORS["dark_blue"],font = self.text_font)
        self.add_button.grid(row=1, column= 1, padx=5, pady=5)
        
        self.add_entry()

        
    def add_entry(self):
        index = len(self.entries)
        placeholder_text=f"Serie {index + 1}"
        
        str_var = ctk.StringVar(value=placeholder_text)
        
        entry = ctk.CTkEntry(self.entries_frame, textvariable=str_var)

        if index == 0:
            entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            self.first_entry = entry 
            
        elif index == 1:
            self.first_entry.grid(row=0, column=0, padx=5, pady=5, columnspan = 1)
            
            entry.grid(row=0, column=1, padx=5, pady=5)
        else:
            entry.grid(row=index // 2, column=index % 2, padx=5, pady=5)
        
        entry.bind("<FocusIn>", lambda e: str_var.set("") if str_var.get() == placeholder_text else None)
        entry.bind("<FocusOut>", lambda e: str_var.set(placeholder_text) if str_var.get() == "" else None)
        
        self.panel_count_var.set(
                self.panel_count_var.get() + 1
            )
        self.boxes.append(entry)
        self.entries.update({placeholder_text : str_var})
        
    def remove_entry(self):
        if len(self.entries) > 1:
            self.panel_count_var.set(
                self.panel_count_var.get() - 1
            )
            entry = self.boxes.pop()
            self.entries.popitem()
            entry.destroy()
            
        if len(self.entries) == 1:
            self.first_entry.grid(row=0, column=0, padx=5, pady=5, columnspan = 2)
            
    def get_series_entries_ref(self):
        return self.entries