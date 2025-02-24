from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                              QLabel, QLineEdit, QComboBox, 
                              QSpinBox, QTextEdit, QGridLayout, QHBoxLayout, 
                              QProgressBar, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap

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
    entry_labels = {
        "Nume complet",
        "CNP"         ,
        "Seria CI"    ,
        "Numar CI"    ,
        "Loc eliberare CI" ,
        "Data eliberare CI",
        "Email"            ,
        "Telefon"          ,
        "Strada"           ,
        "Numar strada"     , 
        "Bloc"             ,
        "Cod postal"       ,
        "Scara"            , 
        "Etaj"             ,
        "Apartament"       ,
        }
        
    def setup_ui(self):
        self.set_title("Date personale")
        
        for label_text in self.entry_labels:
            self.create_entry(label_text)
            
        self.create_judet_combo()

class TargetPlaceScene(FormScene):
    def setup_ui(self):
        ...

class PanelSelectionScene(FormScene):
    def setup_ui(self):
        ...

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