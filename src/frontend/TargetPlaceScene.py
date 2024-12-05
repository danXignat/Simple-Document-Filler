import customtkinter as ctk
from frontend.BackNext import BackNext
from frontend.Scene import Scene
from config import COLORS, TITLE_PADY, judete
from models.SceneType import SceneType

class TargetPlaceScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Loc implementare", pady=TITLE_PADY)
        
        self.entries[SceneType.TargetPlace] = {}
        self.local_entries = self.entries[SceneType.TargetPlace]
        
        self.combo_boxes = {}
        self.local_entries["Judet"], self.combo_boxes["Judet"] = self.create_combo_box("Judet", list(judete.keys()), command=self.get_judet)
        self.local_entries["Localitate"], self.combo_boxes["Localitate"] = self.create_combo_box("Localitate", [])
        
        self.local_entries["Strada"] = self.create_entry("Strada")
        self.local_entries["Numar strada"] = self.create_entry("Numar strada")
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)

    def go_back(self):
        self.controller.switch_scene(SceneType.PersonalData)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.PanelSelection)
        
    def get_judet(self, choice):
        self.combo_boxes["Localitate"].configure(
            state = "normal",
            values = self.get_localitati(choice)
            )
        self.combo_boxes["Localitate"].set("Localitate")
        
        if choice.lower() == "bucuresti" or choice.lower() == "bucurești":
            self.combo_boxes["Localitate"].set("BUCUREȘTI")
            if "Sector" not in self.local_entries:
                self.create_sector_entry()
                
        elif "Sector" in self.local_entries:
            self.combo_boxes["Localitate"].set("Localitate")
            self.combo_boxes["Sector"].destroy()
        
    def get_localitati(self, judet: str):
        localitati = []
        
        for localitate in judete[judet]:
            localitati.append(localitate["name"])
            
        return localitati
    
    def create_sector_entry(self):
        self.local_entries["Sector"], self.combo_boxes["Sector"] = self.create_combo_box("Sector", [str(i) for i in range(1, 7)])