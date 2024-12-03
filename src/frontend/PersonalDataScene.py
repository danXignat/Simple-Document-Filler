import customtkinter as ctk
from frontend.Scene import Scene
from config import COLORS, judete
from models.SceneType import SceneType

FIELDS = {
    "Nume"      : "Nume complet",
    "Email"     : "Adresa de email",
    "Telefon"   : "Număr de telefon",
    "Adresa"    : "Adresa completă",
    "CNP"       : "CNP",
    "Localitate": "Localitate",
    "Sector"    : "Sector"
}

class PersonalDataScene(Scene):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        
        self.label = self.create_label("Date personale", pady=30)
        self.create_form()
        self.create_combo_box("Judet", list(judete.keys()))
        self.create_button("Inapoi", self.go_back, side = "bottom")
        self.create_button("Urmatorul", self.go_next, side = "bottom")
        
    def create_form(self):
        for field, placeholder in FIELDS.items():
            entry = self.create_entry(placeholder)
   
    def go_back(self):
        self.controller.switch_scene(SceneType.MainMenu)
    
    def go_next(self):
        self.controller.switch_scene(SceneType.TargetPlace)
