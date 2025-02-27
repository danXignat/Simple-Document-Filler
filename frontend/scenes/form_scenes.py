from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                              QLabel, QLineEdit, QComboBox, 
                              QSpinBox, QTextEdit, QGridLayout, QHBoxLayout, 
                              QProgressBar, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap

import frontend.items as itm
from config import panels, invertors
from .FormScene import FormScene
    
class MainMenuScene(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.setup_ui()
    
    def setup_ui(self):
        self.buttons = {
            "Client nou"    : None, 
            "Vezi clienti"  : None,
            "Setari"        : None,
            "Ajutor"        : None,
        }
        
        for button_text, button in self.buttons.items():
            btn = QPushButton(button_text)
            btn.setMinimumHeight(50)
            self.main_layout.addWidget(btn)
            
            self.buttons[button_text] = btn
            
class PersonalDataScene(FormScene):
    entry_datas = [
        ("entry", "Nume complet"),
        ("entry", "CNP"),
        ("entry", "Seria CI"),
        ("entry", "Numar CI"),
        ("entry", "Loc eliberare CI"),
        ("entry", "Data eliberare CI"),
        ("entry", "Email"),
        ("entry", "Telefon"),
        ("place", None),
        ("entry", "Strada"),
        ("entry", "Numar strada"),
        ("entry", "Bloc"),
        ("entry", "Cod postal"),
        ("entry", "Scara"),
        ("entry", "Etaj"),
        ("entry", "Apartament"),
    ]

        
    def setup_ui(self):
        self.set_title("Date personale")
        
        self.create_fields()
                    

class TargetPlaceScene(FormScene):
    entry_datas = [
        ("place", None),
        ("entry", "Strada"),
        ("entry", "Numar strada"),
        ("entry", "Numarul de Carte Funciara"),
        ("entry", "Numar topografic al imobilului"),
        ("entry", "Numar cadastral"),
        ("entry", "Suprafata imobilului"),
        ("entry", "Cod unic de identificare POD"),
        ("entry", "Numar contract vanzare cumparare"),
        ("entry", "Persoana emitatoare"),
    ]

    def setup_ui(self):
        self.set_title("Date implementare")
        
        self.create_fields()

class PanelSelectionScene(FormScene):
    entry_datas = [
        ("combo", "Firma", list(panels.keys())),
        ("combo", "Model", []),
        ("combo", "Dispunere", ['N', 'E', 'S', 'V']),
        ("entry", "Eficienta"),
        ("entry", "Interval temperatura"),
        ("entry", "Putere minima"),
        ("entry", "Tehnologie panou"),
        ("entry", "Rama panou"),
        ("entry", "Conectare"),
        ("entry", "Grad protectie"),
        ("entry", "Garantie"),
        ("entry", "Putere nominala"),
        ("entry", "MPPT"),
        ("entry", "Iesire"),
        ("entry", "Frecventa"),
        ("entry", "Umiditate"),
    ]

    def setup_ui(self):
        self.set_title("Date panouri")
        
        self.create_fields()

        self.ids_panel = itm.IDEntryWidget()
        self.main_form_layout.addWidget(self.ids_panel)

        self.combo_boxes["Firma"].currentIndexChanged.connect(self.on_firm_choosed)
        self.combo_boxes["Model"].currentIndexChanged.connect(self.on_model_choosed)

    def on_firm_choosed(self):
        choice = self.combo_boxes["Firma"].currentText()

        items = [model["Model"] for model in panels[choice]]

        self.combo_boxes["Model"].clear()
        self.entries["Eficienta"].clear()
        self.entries["Interval temperatura"].clear()
        self.combo_boxes["Model"].addItems(items)

    def on_model_choosed(self):
        firm = self.combo_boxes["Firma"].currentText()
        choice = self.combo_boxes["Model"].currentText()

        panel_data = next((panel for panel in panels[firm] if panel["Model"] == choice), None)

        self.entries["Eficienta"].setText(panel_data["Eficienta Modul (%)"])
        self.entries["Interval temperatura"].setText(panel_data["Interval de temperatura operare (°C)"])

class InvertorSelectionScene(FormScene):
    def setup_ui(self):
        ...

class SmartMeterSelectionScene(FormScene):
    def setup_ui(self):
       ...

class SummaryScene(FormScene):
    def setup_ui(self):
        ...

class ViewClientsScene(FormScene):
    def setup_ui(self):
        ...