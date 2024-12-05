from config import *
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from models.SceneType import SceneType

class InvertorSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza invertor", pady=TITLE_PADY)
        
        self.entries[SceneType.InvertorSelection] = {}
        self.local_entries = self.entries[SceneType.InvertorSelection]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(invertors.keys()), command=self.firm_choice)
        self.local_entries["Seria"], self.combo_boxes["Seria"] = self.create_combo_box("Seria modelului", [], command=self.model_choice)                
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
    
    def go_back(self):
        self.controller.switch_scene(SceneType.PanelSelection)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.SmartMeterSelection)
    
    def firm_choice(self, choice):
        self.combo_boxes["Seria"].configure(
            state = "normal",
            values = [seria for seria in invertors[choice].keys()]
            )
        self.combo_boxes["Seria"].set("Seria")
        
    def model_choice(self, choice):
        firm = self.combo_boxes["Firma"].get()
        
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Model"] for model in invertors[firm][choice]]
            )
        self.combo_boxes["Model"].set("Model")

    