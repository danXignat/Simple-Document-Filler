from typing import Dict
from icecream import ic
from tkinter import filedialog
import copy
import os

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
        self.controller.switch_scene("Date Smart Meter")
    
    def submit(self):
        self.save_client()
        data = self.export_data()
        
        ic(data[0])
        ic(data[1])
        
        file_path = filedialog.askdirectory()
        file_path += os.sep
        submit_handler.submit(data, file_path)
    
    def update_data(self):
        self.data_summary.update_data()
    
    def get_dict(self) -> Dict:
        data = {}
        
        for label, category in self.entries.items():
            data[label] = {key: value.get() for key, value in category.items()}

        return data
    
    def save_client(self):
        with open(CLIENTS_PATH, "r") as file:
            clients_data = json.load(file)
            
        formatted_data = self.get_dict()
        data = {
            "id": len(clients_data) + 1,
            "name": formatted_data["Date personale"]["Nume complet"],
            "data": formatted_data
        }
        
        clients_data.append(data)
        with open(CLIENTS_PATH, 'w') as file:
            json.dump(clients_data, file, indent=4)

    def export_data(self):
        data = {}
        series = {}
        
        for category, items in self.entries.items():
            category_name = category if isinstance(category, str) else category.value
            
            if "Serii" in category_name:
                series[f"[{category_name}]"] = [value.get() if key != value.get() else "-" for key, value in items.items()]

            elif category_name == "Date implementare":
                data.update({
                    f"[{label}_target]" if label in {"Judet", "Localitate", "Numar strada", "Strada"}
                    else f"[{label}]": value.get() if label != value.get() else "-"
                    for label, value in items.items()
                })
            
            elif category_name == "Date panouri":
                data.update({
                    f"[{label}_panel]" : value.get() if label != value.get() else "-"
                    for label, value in items.items()
                })
            
            elif category_name == "Date invertor":
                data.update({
                    f"[{label}_invertor]" : value.get() if label != value.get() else "-"
                    for label, value in items.items()
                })
            
            elif category_name == "Date Smart Meter":
                data.update({
                    f"[{label}_smartmeter]" : value.get() if label != value.get() else "-"
                    for label, value in items.items()
                })
            
            else:
                data.update({f"[{label}]": value.get() if label != value.get() else "-" for label, value in items.items()})

        return (data, series)
    