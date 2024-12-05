from config import *
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from models.SceneType import SceneType

class SmartMeterSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza Smart Meter", pady=TITLE_PADY)
        
        self.entries[SceneType.SmartMeterSelection] = {}
        self.local_entries = self.entries[SceneType.SmartMeterSelection]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(smart_meters.keys()), command=self.firm_choice)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])                
                
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def go_back(self):
        self.controller.switch_scene(SceneType.InvertorSelection)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.Summary)
    
    def firm_choice(self, choice):
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Smart Meter"] for model in smart_meters[choice]]
            )
        self.combo_boxes["Model"].set("Model")