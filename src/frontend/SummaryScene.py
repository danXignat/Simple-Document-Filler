from config import *
from frontend.Scene import Scene
from frontend.BackNext import BackNext
from models.SceneType import SceneType
from frontend.DataSummary import DataSummary


class SummaryScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Rezumat", pady=TITLE_PADY)
        
        self.data_summary = DataSummary(self, self.entries)
        self.data_summary.pack(padx = 10, pady = 10, fill = "both", expand=True)        
        
        self.bacl_next = BackNext(self, self.go_back, self.submit, self._fg_color, next_label="Submit")
        
    def go_back(self):
        self.controller.switch_scene(SceneType.SmartMeterSelection)
    
    def submit(self):
        print("sub")
    
    def update_data(self):
        self.data_summary.update_data()
    