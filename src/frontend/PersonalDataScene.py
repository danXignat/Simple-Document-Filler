import customtkinter as ctk
from frontend.Scene import Scene
from config import COLORS, judete
from models.SceneType import SceneType

text_entries = {
    "Nume"      : "Nume complet",
    "Email"     : "Adresa de email",
    "Telefon"   : "Număr de telefon",
    "Adresa"    : "Adresa completă",
    "CNP"       : "CNP",
    "Sector"    : "Sector"
}

combo_box_entries  = {
    "Localitate": "Localitate",
    "Judet"     : "Judet"
}

class PersonalDataScene(Scene):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.label = self.create_label("Date personale", pady=30)
        self.create_form()
        
        self.entries["Judet"] = self.create_combo_box("Judet", list(judete.keys()), command=self.get_judet)
        self.entries["Localitate"] = self.create_combo_box("Localitate", [])
        
        self.create_button("Inapoi", self.go_back, side = "bottom")
        self.create_button("Urmatorul", self.go_next, side = "bottom")
        
    def create_form(self):
        for field, placeholder in text_entries.items():
            entry = self.create_entry(placeholder)
   
    def get_judet(self, choice):
        self.entries["Localitate"].configure(
            state = "normal",
            values = self.get_localitati(choice)
            )
        self.entries["Localitate"].set("Localitate")
        
    def go_back(self):
        self.controller.switch_scene(SceneType.MainMenu)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.TargetPlace)
        
    def get_localitati(self, judet: str):
        localitati = []
        
        for localitate in judete[judet]:
            localitati.append(localitate["name"])
            
        return localitati
