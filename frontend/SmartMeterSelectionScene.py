import customtkinter as ctk

from config import *
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from models.SceneType import SceneType

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class SmartMeterSelectionScene(Scene):
    entry_labels = [
        "Eficienta",
        "Grad protectie",
        "Interval temperatura",
        "Garantie",
        "Frecventa",
        "Umiditate",
        "Putere nominala",
    ]
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        self.create_label("Selecteaza Smart Meter", pady=TITLE_PADY)
        
        self.entries["Date Smart Meter"] = {}
        self.local_entries = self.entries["Date Smart Meter"]
        self.combo_boxes = {}
        
        self.frame = ctk.CTkScrollableFrame(self, fg_color=self._fg_color, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
                
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(smart_meters.keys()), command=self.firm_choice, parent = self.frame)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [], command=self.model_chosen, parent = self.frame)                
        
        for entry in self.entry_labels:
            self.local_entries[entry] = self.create_entry(entry, parent = self.frame)
        
        smart_meters_count = IDSCount(self.frame, "Numar Smart Meters")        
        self.local_entries["Numar Smart Meters"] = smart_meters_count.count_var
        
        self.entries["Serii Smart Meters"] = {}
        self.ids_frame = IDSFrame(
            self.frame, self.entries["Serii Smart Meters"],
            fg_color=self._fg_color, 
            panel_count_var=smart_meters_count.count_var,
            height=50
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
        
        self.frame.pack(padx = 5, fill = 'both', expand=True)
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def go_back(self):
        self.controller.switch_scene("Date invertor")
    
    def go_next(self):
        self.controller.switch_scene("Rezumat")
    
    def firm_choice(self, choice):
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Smart Meter"] for model in smart_meters[choice]]
            )
        self.combo_boxes["Model"].set("Model")
        self.set_entries_to_def()
        
    def model_chosen(self, choice):
        firm = self.combo_boxes["Firma"].get()
        
        smart_meter_data = next((smart_meter for smart_meter in smart_meters[firm] if smart_meter["Smart Meter"] == choice), None)
        
        self.local_entries["Eficienta"].set(smart_meter_data["Eficienta"])
        self.local_entries["Interval temperatura"].set(smart_meter_data["Interval Functionare"])
        self.local_entries["Garantie"].set(smart_meter_data["Garantie"])
        self.local_entries["Grad protectie"].set(smart_meter_data["Grad Protectie"])
        self.local_entries["Frecventa"].set(smart_meter_data["Frecventa"])
        self.local_entries["Umiditate"].set(smart_meter_data["Umiditate Maxima"])
        
    def set_entries_to_def(self):
        for entry in self.entry_labels:
            self.local_entries[entry].set(entry)