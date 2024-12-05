import customtkinter as ctk
from frontend.Scene import Scene
from config import COLORS, TITLE_PADY, judete
from models.SceneType import SceneType
from frontend.BackNext import BackNext


class PersonalDataScene(Scene):
    text_entries = {
        "Nume"      : "Nume complet",
        "Email"     : "Adresa de email",
        "Telefon"   : "Număr de telefon",
        "Adresa"    : "Adresa completă",
        "NrStrada"  : "Numar strada", 
        "CNP"       : "CNP",
    }
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        self.entries[SceneType.PersonalData] = {}
        self.local_entries = self.entries[SceneType.PersonalData]
        
        self.label = self.create_label("Date personale", pady=TITLE_PADY)
        
        self.create_form()
        
        self.combo_boxes = {}
        self.local_entries["Judet"], self.combo_boxes["Judet"] = self.create_combo_box("Judet", list(judete.keys()), command=self.get_judet)
        self.local_entries["Localitate"], self.combo_boxes["Localitate"] = self.create_combo_box("Localitate", [])
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def create_form(self):
        for field, placeholder in self.text_entries.items():
            self.local_entries[field] = self.create_entry(placeholder)
        
    def go_back(self):
        self.controller.switch_scene(SceneType.MainMenu)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.TargetPlace)
   
    def get_judet(self, choice):
        self.combo_boxes["Localitate"].configure(
            state = "normal",
            values = self.get_localitati(choice)
            )
        self.combo_boxes["Localitate"].set("Localitate")
        
        if choice.lower() == "bucuresti" or choice.lower() == "bucurești":
            self.combo_boxes["Localitate"].set("BUCUREȘTI")
            if "Sector" not in self.combo_boxes:
                self.create_sector_entry()
                
        elif "Sector" in self.combo_boxes:
            self.combo_boxes["Localitate"].set("Localitate")
            self.combo_boxes["Sector"].destroy()
        
    def get_localitati(self, judet: str):
        localitati = []
        
        for localitate in judete[judet]:
            localitati.append(localitate["name"])
            
        return localitati
    
    def create_sector_entry(self):
        self.local_entries["Sector"], self.combo_boxes["Sector"] = self.create_combo_box("Sector", [str(i) for i in range(1, 7)])
