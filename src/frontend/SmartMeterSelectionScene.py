from config import *
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from models.SceneType import SceneType

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class SmartMeterSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza Smart Meter", pady=TITLE_PADY)
        
        self.entries["Date Smart Meter"] = {}
        self.local_entries = self.entries["Date Smart Meter"]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(smart_meters.keys()), command=self.firm_choice)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])                
        
        smart_meters_count = IDSCount(self, "Numar Smart Meters")        
        self.local_entries["Numar Smart Meters"] = smart_meters_count.count_var
        
        self.entries["Serii Smart Meters"] = {}
        self.ids_frame = IDSFrame(
            self, self.entries["Serii Smart Meters"],
            fg_color=self._fg_color, 
            panel_count_var=smart_meters_count.count_var,
            height=50
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
        
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