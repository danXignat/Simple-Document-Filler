from config import *

from frontend.Scene import Scene
from models.SceneType import SceneType
from frontend.BackNext import BackNext

from frontend.IDSCount import IDSCount
from frontend.IDSFrame import IDSFrame

class InvertorSelectionScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Selecteaza invertor", pady=TITLE_PADY)
        
        self.entries[SceneType.InvertorSelection] = {}
        self.local_entries = self.entries[SceneType.InvertorSelection]
        
        self.combo_boxes = {}
        self.local_entries["Firma"], self.combo_boxes["Firma"] = self.create_combo_box("Firma", list(invertors.keys()), command=self.firm_choice)
        self.local_entries["Gama"], self.combo_boxes["Gama"] = self.create_combo_box("Gama", [], command=self.model_choice)                
        self.local_entries["Model"], self.combo_boxes["Model"] = self.create_combo_box("Model", [])
        self.local_entries["ID data logger"] = self.create_entry("ID data logger")
        self.local_entries["Parola invertor"] = self.create_entry("Parola invertor")
        
        smart_meters_count = IDSCount(self, "Numar invertoare")        
        self.local_entries["Numar invertoare"] = smart_meters_count.count_var
        
        self.entries["Serii invertoare"] = {}
        self.ids_frame = IDSFrame(
            self, self.entries["Serii invertoare"],
            fg_color=self._fg_color, 
            panel_count_var=smart_meters_count.count_var,
            height=50
            )
        
        self.ids_frame.pack(padx = 0, pady = 5, fill="none", expand=False)
            
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
    
    def go_back(self):
        self.controller.switch_scene(SceneType.PanelSelection)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.SmartMeterSelection)
    
    def firm_choice(self, choice):
        self.combo_boxes["Gama"].configure(
            state = "normal",
            values = [seria for seria in invertors[choice].keys()]
            )
        self.combo_boxes["Gama"].set("Gama")
        self.combo_boxes["Model"].set("Model")
        
    def model_choice(self, choice):
        firm = self.combo_boxes["Firma"].get()
        
        self.combo_boxes["Model"].configure(
            state = "normal",
            values = [model["Model"] for model in invertors[firm][choice]]
            )
        self.combo_boxes["Model"].set("Model")

    