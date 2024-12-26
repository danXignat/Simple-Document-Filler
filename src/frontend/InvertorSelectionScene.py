import customtkinter as ctk

from config import *

from frontend.Scene import Scene
from models.SceneType import SceneType
from frontend.BackNext import BackNext

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class InvertorSelectionScene(Scene):
    entry_labels = [
        "Eficienta",
        "Grad protectie",
        "Interval temperatura",
        "Garantie",
        "Frecventa",
        "Putere nominala",
        "ID data logger",
        "Parola invertor",
        "Umiditate"
    ]
    
    json_labels = [
        "Eficiență",
        "Interval de temperatură",
        "Garanție",
        "Grad de protecție",
        "Frecvență",
        "Putere nominală instalată",
        "Umiditate maximă"
    ]
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        self.create_label("Selecteaza invertor", pady=TITLE_PADY)
        
        self.entries["Date invertor"] = {}
        self.combo_boxes = {}
        self.local_entries = self.entries["Date invertor"]
        
        self.frame = ctk.CTkScrollableFrame(self, fg_color=self._fg_color, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(invertors.keys()), command=self.firm_choice, parent = self.frame)
        self.local_entries["Gama"], self.combo_boxes["Gama"] = self.create_combo_box("Gama", [], command=self.model_choice, parent = self.frame)                
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [], command=self.model_chosen, parent = self.frame)
        
        for entry in self.entry_labels:
            self.local_entries[entry] = self.create_entry(entry, parent = self.frame)
        
        smart_meters_count = IDSCount(self.frame, "Numar invertoare")        
        self.local_entries["Numar invertoare"] = smart_meters_count.count_var
        
        self.entries["Serii invertoare"] = {}
        self.ids_frame = IDSFrame(
            self.frame, self.entries["Serii invertoare"],
            fg_color=self._fg_color, 
            panel_count_var=smart_meters_count.count_var,
            height=50
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
        
        self.frame.pack(padx = 5, fill = 'both', expand=True)
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
    
    def go_back(self):
        self.controller.switch_scene("Date panouri")
    
    def go_next(self):
        self.controller.switch_scene("Date Smart Meter")
    
    def firm_choice(self, choice):
        self.combo_boxes["Gama"].configure(
            state = "normal",
            values = [seria for seria in invertors[choice].keys()]
            )
        self.combo_boxes["Gama"].set("Gama")
        self.combo_boxes["Model"].set("Model")
        self.set_entries_to_def()
        
    def model_choice(self, choice):
        firm = self.combo_boxes["Firma"].get()
        gama = self.combo_boxes["Gama"].get()
        
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Model"] for model in invertors[firm][choice]]
            )
        self.combo_boxes["Model"].set("Model")
        self.set_entries_to_def()
        
    def model_chosen(self, choice):
        firm = self.combo_boxes["Firma"].get()
        gama = self.combo_boxes["Gama"].get()
        
        invertor_data = next((invertor for invertor in invertors[firm][gama] if invertor["Model"] == choice), None)
        
        self.local_entries["Eficienta"].set(invertor_data["Eficiență"])
        self.local_entries["Interval temperatura"].set(invertor_data["Interval de temperatură"])
        if "Garanție" in invertor_data:
            self.local_entries["Garantie"].set(invertor_data["Garanție"])
        self.local_entries["Grad protectie"].set(invertor_data["Grad de protecție"])
        self.local_entries["Frecventa"].set(invertor_data["Frecvență"])
        self.local_entries["Putere nominala"].set(invertor_data["Putere nominală instalată"])
        self.local_entries["Umiditate"].set(invertor_data["Umiditate maximă"])
        
    def set_entries_to_def(self):
        for entry in self.entry_labels:
            self.local_entries[entry].set(entry)

    