from config import *
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from models.SceneType import SceneType
from frontend.PanelIDSFrame import PanelIDSFrame

class PanelSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza panouri", pady=TITLE_PADY)
        self.entries[SceneType.PanelSelection] = {}
        self.local_entries = self.entries[SceneType.PanelSelection]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(panels.keys()), command=self.firm_choice)
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])                
                
        self.entries["Panouri"] = {}
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
        self.ids_frame = PanelIDSFrame(self, self.entries["Panouri"], fg_color=self._fg_color)
        self.ids_frame.pack(padx = 0, pady = 20, fill="none", expand=False)
        
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