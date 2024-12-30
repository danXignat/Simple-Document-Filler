import customtkinter as ctk
import datetime

from frontend.BackNext import BackNext
from frontend.IDSCount import IDSCount
from frontend.Scene import Scene
from frontend.CalendarEntry import DateEntry
from config import COLORS, TITLE_PADY, judete
from models.SceneType import SceneType

class TargetPlaceScene(Scene):
    text_entries = [
        "Numarul de Carte Funciara",
        "Numar topografic al imobilului",
        "Numar cadastral",
        "Suprafata imobilului",
        "Cod unic de identificare POD",
        "Numar contract vanzare cumparare",
        "Persoana emitatoare",
        "Strada",
        "Numar strada",
    ]
    
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label("Loc implementare", pady=TITLE_PADY)
        
        self.entries["Date implementare"] = {}
        self.local_entries = self.entries["Date implementare"]
        self.combo_boxes = {}
        
        self.prob_dates = [None, None]
        self.prob_calendars = [None, None]
        
        for text in self.text_entries:
            self.local_entries[text] = self.create_entry(text)
        
        dates_frame = ctk.CTkFrame(self, fg_color=self._fg_color)
        
        calendar = DateEntry(dates_frame, "Data incepere probe", row=0,  fg_color=self._fg_color)
        self.prob_calendars[0] = calendar
        calendar.update_signal.connect(self.handle_date_update)
        self.local_entries["Data incepere probe"] = calendar.string_var
        # calendar.pack(fill = 'x', pady=10, anchor = 'center')
        
        calendar = DateEntry(dates_frame, "Data terminare probe", row=1, fg_color=self._fg_color)
        self.prob_calendars[1] = calendar
        calendar.update_signal.connect(self.handle_date_update)
        self.local_entries["Data terminare probe"] = calendar.string_var
        # calendar.pack(fill = 'x', pady=10, anchor = 'center')
        
        dates_frame.pack(pady = 10)
        
        count_panel = IDSCount(self, "Durata probe")
        self.local_entries["Durata probe"] = count_panel.count_var
        count_panel.pack(pady=10)
        
        self.local_entries["Judet"], self.combo_boxes["Judet"] = self.create_combo_box("Judet", list(judete.keys()), command=self.get_judet)
        self.local_entries["Localitate"], self.combo_boxes["Localitate"] = self.create_combo_box("Localitate", [])
        self.local_entries["Sector"] = ctk.StringVar(value = "Sector")
        
        self.back_next_buttons = BackNext(self, self.go_back, self.go_next, self._fg_color)
        
    def handle_date_update(self, label, date):
        match label:
            case "Data incepere probe":
                self.prob_dates[0] = date
                self.prob_calendars[1].calendar.config(mindate = date + datetime.timedelta(days = 1))
            
            case "Data terminare probe":
                self.prob_dates[1] = date
                self.prob_calendars[0].calendar.config(maxdate = date - datetime.timedelta(days = 1))
        
        if self.prob_dates[0] and self.prob_dates[1]:
            self.local_entries["Durata probe"].set(
                (self.prob_dates[1] - self.prob_dates[0]).days
            )
        
    def go_back(self):
        self.controller.switch_scene("Date personale")
    
    def go_next(self):
        self.controller.switch_scene("Date panouri")
        
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
        self.local_entries["Sector"], self.combo_boxes["Sector"] = self.create_combo_box("Sector", [str(i) for i in range(1, 7)], str_var = self.local_entries["Sector"])