import customtkinter as ctk
from frontend.Scene import Scene
from config import COLORS, judete
from models.SceneType import SceneType

FIELDS = {
    "Adresa"    : "Adresa completă",
}

class TargetPlaceScene(Scene):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.create_label("Date personale")
        self.create_entry("Strada")
        self.create_combo_box("Judet", list(judete.keys()))
        
        self.create_button("Inapoi", self.go_back, side = "bottom")
        
    def go_back(self):
        self.controller.switch_scene(SceneType.PersonalData)