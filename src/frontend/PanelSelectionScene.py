import customtkinter as ctk

from config import *
from models.SceneType import SceneType

from frontend.Scene import Scene
from frontend.BackNext import BackNext

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class PanelSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza panouri", pady=TITLE_PADY)
        self.entries[SceneType.PanelSelection] = {}
        self.local_entries = self.entries[SceneType.PanelSelection]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(panels.keys()), command=self.firm_choice)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])                
        self.local_entries["Dispunere panouri"], self.combo_boxes["Dispunere panouri"] = self.create_combo_box("Dispunere panouri", ["SUD", "NORD", "EST", "VEST"])
        
        panel_count = IDSCount(self, "Numar panouri")        
        self.local_entries["Numar panouri"] = panel_count.count_var
        
        self.entries["Serii panouri"] = {}
        self.ids_frame = IDSFrame(
            self, self.entries["Serii panouri"],
            fg_color=self._fg_color,
            panel_count_var=panel_count.count_var,
            height=250
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def go_back(self):
        self.controller.switch_scene(SceneType.TargetPlace)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.InvertorSelection)
    
    def firm_choice(self, choice):
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Model"] for model in panels[choice]]
            )
        self.combo_boxes["Model"].set("Model")