import customtkinter as ctk

from config import *
from models.SceneType import SceneType

from frontend.Scene import Scene
from frontend.BackNext import BackNext

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class PanelSelectionScene(Scene):
    entry_labels = [
        "Eficienta",
        "Interval temperatura",
        "Putere minima",
        "Tehnologie panou",
        "Rama panou",
        "Conectare",
        "Grad protectie",
        "Garantie",
        "Putere nominala",
        "MPPT",
        "Iesire",
        "Frecventa",
        "Umiditate",
    ]
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza panouri", pady=TITLE_PADY)
        self.entries["Date panouri"] = {}
        self.combo_boxes = {}
        self.local_entries = self.entries["Date panouri"]
        
        self.frame = ctk.CTkScrollableFrame(self, fg_color=self._fg_color, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(panels.keys()), command=self.firm_choice, parent=self.frame)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [], command = self.model_choice, parent=self.frame)                
        self.local_entries["Dispunere panouri"], self.combo_boxes["Dispunere panouri"] = self.create_combo_box("Dispunere panouri", ["SUD", "NORD", "EST", "VEST"], parent=self.frame)
        
        for entry in self.entry_labels:
            self.local_entries[entry] = self.create_entry(entry, parent=self.frame)
        
        panel_count = IDSCount(self.frame, "Numar panouri")        
        self.local_entries["Numar panouri"] = panel_count.count_var
        
        self.entries["Serii panouri"] = {}
        self.ids_frame = IDSFrame(
            self.frame, self.entries["Serii panouri"],
            fg_color=self._fg_color,
            panel_count_var=panel_count.count_var,
            height=250
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
        
        self.frame.pack(padx = 5, fill = 'both', expand=True)
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def go_back(self):
        self.controller.switch_scene("Date implementare")
    
    def go_next(self):
        self.controller.switch_scene("Date invertor")
    
    def firm_choice(self, choice):
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Model"] for model in panels[choice]]
            )
        self.combo_boxes["Model"].set("Model")
        self.local_entries["Eficienta"].set("Eficienta")
        self.local_entries["Interval temperatura"].set("Interval temperatura")
        
    def model_choice(self, choice):
        firm = self.combo_boxes["Firma"].get()
        
        panel_data = next((panel for panel in panels[firm] if panel["Model"] == choice), None)
        
        self.local_entries["Eficienta"].set(panel_data["Eficienta Modul (%)"])
        self.local_entries["Interval temperatura"].set(panel_data["Interval de temperatura operare (°C)"])