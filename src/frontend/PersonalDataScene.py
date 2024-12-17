import customtkinter as ctk
from frontend.Scene import Scene
from config import COLORS, TITLE_PADY, judete
from models.SceneType import SceneType
from frontend.BackNext import BackNext


class PersonalDataScene(Scene):
    text_entries = {
        "Nume"          : "Nume complet",
        "Email"         : "Adresa de email",
        "Telefon"       : "Număr de telefon",
        "Adresa"        : "Adresa completă",
        "Strada"        : "Strada",
        "Numar strada"  : "Numar strada", 
        "Bloc"          : "Bloc",
        "Scara"         : "Scara",
        "Etaj"          : "Etaj",
        "Apartament"    : "Apartament",
        "CNP"           : "CNP",
        "Seria CI"      : "Seria CI",
        "Numar CI"      : "Numar CI",
        "Loc eliberare CI" : "Loc eliberare CI",
        "Data eliberare CI" : "Data eliberare CI",
    }
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        self.entries[SceneType.PersonalData] = {}
        self.local_entries = self.entries[SceneType.PersonalData]
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color=self._fg_color, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        
        self.label = self.create_label("Date personale", pady=TITLE_PADY)
        
        self.create_form()
        
        self.combo_boxes = {}
        self.local_entries["Judet"], self.combo_boxes["Judet"] = self.create_combo_box("Judet", list(judete.keys()), command=self.get_judet, parent=self.scrollable_frame)
        self.local_entries["Localitate"], self.combo_boxes["Localitate"] = self.create_combo_box("Localitate", [], parent=self.scrollable_frame)
        self.local_entries["Sector"] = ctk.StringVar(value = "Sector")
        
        self.scrollable_frame.pack(padx = 5, fill = 'both', expand=True)
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def create_form(self):
        for field, placeholder in self.text_entries.items():
            self.local_entries[field] = self.create_entry(placeholder, parent=self.scrollable_frame)
        
    def go_back(self):
        self.controller.switch_scene(SceneType.DocumentsData)
    
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
        self.local_entries["Sector"], self.combo_boxes["Sector"] = self.create_combo_box("Sector", [str(i) for i in range(1, 7)], parent = self.scrollable_frame, str_var = self.local_entries["Sector"])
