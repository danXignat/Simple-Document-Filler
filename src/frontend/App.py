from turtle import window_width
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
from typing import Dict
from icecream import ic

from config import *
from frontend import *
from frontend.BackNext import BackNext
from models.SceneType import SceneType

scenes_constr = {
    "Meniu principal"   : MainMenuScene,
    "Date personale"    : PersonalDataScene,
    "Date implementare" : TargetPlaceScene,
    "Date panouri"      : PanelSelectionScene,
    "Date invertor"     : InvertorSelectionScene,
    "Date Smart Meter"  : SmartMeterSelectionScene,
    "Rezumat"           : SummaryScene,
    "Clienti"           : ViewClientsScene,
}

BackNext.frame_number = len(scenes_constr) - 2

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        top_width = WINDOW_WIDTH  
        top_height = WINDOW_HEIGHT
        
        x = (screen_width - top_width) // 8
        y = (screen_height - top_height) // 2
        
        self.geometry(f"{top_width}x{top_height}+{x}+{y}")
        self.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.iconbitmap(LOGO_PATH)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.scene_container = ctk.CTkFrame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, corner_radius=0)
        self.scene_container.grid(row=0, column=0, sticky="nsew")
        
        self.scene_container.grid_rowconfigure(0, weight=1)
        self.scene_container.grid_columnconfigure(0, weight=1)
        
        current_day = datetime.now()
        formatted_day = current_day.strftime("%d-%m-%Y")
        
        self.data_container = {}
        self.data_container["Date documente"] = {"Data intocmire": ctk.StringVar(value=formatted_day)}
        self.scenes = {}
        
        self.init_scenes()
        
        self.default_data = self.get_dict()
        
        self.switch_scene("Meniu principal")
        
    def init_scenes(self):
        for scene_type, SceneClass in scenes_constr.items():
            scene = SceneClass(
                parent=self.scene_container,
                controller=self,
                data_container = self.data_container
                )
            
            self.scenes[scene_type] = scene
            
            scene.grid(row=0, column=0, padx = 20, pady = 20, sticky="nsew")

    def switch_scene(self, scene_type: str):
        scene = self.scenes[scene_type]
        
        if isinstance(scene, SummaryScene):
            scene.update_data()
        
        if isinstance(scene, ViewClientsScene):
            scene.update_clients()
                
        scene.tkraise()
    
    def reinitiliase_series(self):
        scenes_to_visit = {"Date panouri": "Serii panouri", "Date invertor": "Serii invertoare", "Date Smart Meter": "Serii Smart Meters"}
        
        for scene, data_cat in scenes_to_visit.items():
            while len(self.default_data[data_cat]) > len(self.data_container[data_cat]):
                self.scenes[scene].ids_frame.add_entry()
            
            while len(self.default_data[data_cat]) < len(self.data_container[data_cat]):
                self.scenes[scene].ids_frame.remove_entry()
                
        if "Sector" in self.scenes["Date personale"].combo_boxes:
            self.scenes["Date personale"].combo_boxes["Sector"].destroy()
            self.scenes["Date personale"].combo_boxes.pop("Sector")
        
        if "Sector" in self.scenes["Date implementare"].combo_boxes:
            self.scenes["Date implementare"].combo_boxes["Sector"].destroy()
            self.scenes["Date implementare"].combo_boxes.pop("Sector")
        
    def reinitialise(self):
        self.reinitiliase_series()
        
        for (label1, category1), (label2, category2) in zip(self.default_data.items(), self.data_container.items()):
            for (key1, val1), (key2, val2) in zip(category1.items(), category2.items()):
                val2.set(val1)

    def get_dict(self) -> Dict:
        data = {}
        
        for label, category in self.data_container.items():
            data[label] = {key: value.get() for key, value in category.items()}

        return data
