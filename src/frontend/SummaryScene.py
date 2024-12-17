from typing import Dict
from icecream import ic

from frontend.Scene import Scene
from frontend.BackNext import BackNext
from frontend.DataSummary import DataSummary
from models.SceneType import SceneType
from config import *

from backend import submit_handler

class SummaryScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Rezumat", pady=TITLE_PADY)
        
        self.data_summary = DataSummary(self, self.entries)
        self.data_summary.pack(padx = 10, pady = 10, fill = "both", expand=True)        
        
        self.bacl_next = BackNext(self, self.go_back, self.submit, self._fg_color, next_label="Submit", is_submit=True)
        
    def go_back(self):
        self.controller.switch_scene(SceneType.SmartMeterSelection)
    
    def submit(self):
        data = self.export_data()
        
        ic(data[0])
        ic(data[1])
        
        submit_handler.submit(data)
    
    def update_data(self):
        self.data_summary.update_data()
        
    def export_data(self):
        data = {}
        series = {}
        
        for category, items in self.entries.items():
            category_name = category if isinstance(category, str) else category.value
            
            if "Serii" in category_name:
                series[f"[{category_name}]"] = [value.get() for value in items.values()]

            elif category_name == "Date implementare":
                data.update({
                    f"[{label}_target]" if label in {"Judet", "Localitate", "Numar strada", "Strada"}
                    else f"[{label}]": value.get()
                    for label, value in items.items()
                })
            
            elif category_name == "Date panouri":
                data.update({
                    f"[{label}_panel]" : value.get()
                    for label, value in items.items()
                })
            
            elif category_name == "Date invertor":
                data.update({
                    f"[{label}_invertor]" : value.get()
                    for label, value in items.items()
                })
            
            elif category_name == "Date Smart Meter":
                data.update({
                    f"[{label}_smartmeter]" : value.get()
                    for label, value in items.items()
                })
            
            else:
                data.update({f"[{label}]": value.get() for label, value in items.items()})

        return (data, series)
    