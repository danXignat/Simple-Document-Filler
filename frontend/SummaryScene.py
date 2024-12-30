from typing import Dict
from icecream import ic
from tkinter import filedialog, messagebox
import copy
import os
import threading
import json

from frontend.Scene import Scene
from frontend.BackNext import BackNext
from frontend.ExportWindow import ExportWindow
from frontend.DataSummary import DataSummary
from models.SceneType import SceneType
import config

from backend import submit_handler

class SummaryScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Rezumat", pady=config.TITLE_PADY)
        
        self.data_summary = DataSummary(self, self.entries)
        
        self.data_summary.pack(padx = 10, pady = 10, fill = "both", expand=True)        
        
        self.bacl_next = BackNext(self, self.go_back, self.submit, self._fg_color, next_label="Submit", is_submit=True)
        
        main_menu_button = self.create_button("Meniu principal", command=self.go_main_menu)
        
    def go_main_menu(self):
        result = messagebox.askyesno("Confirmare", "Esti sigur? Vei pierde progresul!")
        if result:
            self.controller.reinitialise()
            self.controller.switch_scene("Meniu principal")
            print("Reset")
        else:
            print("Action canceled!")
    
    def go_back(self):
        self.controller.switch_scene("Date Smart Meter")
    
    def submit(self):
        self.save_client()
        data = self.export_data()
        
        ic(data[0])
        ic(data[1])
        
        file_path = filedialog.askdirectory()
        
        if file_path:
            file_path += os.sep
            
            export_window = ExportWindow(self.controller)
            
            submit_task = threading.Thread(target = submit_handler.submit, args = (data, file_path, export_window))
            submit_task.start()
        
        
    def update_data(self):
        self.data_summary.update_data()
    
    def save_client(self):
        with open(config.CLIENTS_PATH, "r") as file:
            clients_data = json.load(file)
            
        formatted_data = self.controller.get_dict()
        data = {
            "id": len(clients_data) + 1,
            "name": formatted_data["Date personale"]["Nume complet"],
            "data": formatted_data
        }
        
        clients_data.append(data)
        with open(config.CLIENTS_PATH, 'w') as file:
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
                    f"[{label}_target]" if label in {"Judet", "Localitate", "Numar strada", "Strada", "Sector"}
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
    