import PySide6.QtWidgets as widg
import PySide6.QtCore as core
import PySide6.QtGui as gui

from abc import ABCMeta, ABC, abstractmethod

import frontend.items as itm
from config import judete

class FormScene(widg.QWidget):
    entry_datas = []
    
    def __init__(self, progres_increment: int, parent=None):
        super().__init__(parent)
        self.progres_increment = progres_increment
        self.entries    : dict[str, widg.QLineEdit] = {}
        self.combo_boxes: dict[str, widg.QComboBox] = {}
        
        self.main_layout = widg.QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
       
        self.title = widg.QLabel("Placeholder")
        self.main_layout.addWidget(self.title)
       
        # Create a scroll area
        self.scroll_area = widg.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarAsNeeded)

        # Create the form container
        self.form_container = widg.QWidget()
        self.main_form_layout = widg.QVBoxLayout(self.form_container)

        self.form_layout = widg.QFormLayout()
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setVerticalSpacing(10)  # Space between rows
        # self.form_layout.setColumnStretch(1, 1)  # Make inputs expand
        
        self.main_form_layout.addLayout(self.form_layout)
        self.scroll_area.setWidget(self.form_container)
        self.main_layout.addWidget(self.scroll_area, 1)  # Give stretch factor of 1
       
        # Set up navigation at the bottom
        self._setup_navigation()
       
        self.setup_ui()
        
    @abstractmethod
    def setup_ui(self):
        ...
    
    def _setup_navigation(self):
        """ Create navigation container """
        self.nav_container = widg.QWidget()
        nav_layout = widg.QHBoxLayout(self.nav_container)
        
        self.back_btn = widg.QPushButton("Inapoi")
        self.next_btn = widg.QPushButton("Urmatorul")
        
        self.progress_bar = widg.QProgressBar()
        self.progress_bar.setValue(self.progres_increment)
        self.progress_bar.setTextVisible(False)
        
        self.logo_label = widg.QLabel()
        logo_pixmap = gui.QPixmap("static/logo.ico")
        self.logo_label.setPixmap(logo_pixmap.scaled(24, 24, core.Qt.KeepAspectRatio, core.Qt.SmoothTransformation))
        
        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.progress_bar, 1)  # Progress bar takes remaining space
        nav_layout.addWidget(self.logo_label)
        nav_layout.addWidget(self.next_btn)
        
        self.main_layout.addWidget(self.nav_container)

    def set_title(self, title: str):
        self.title.setText(title)
            
    def create_entry(self, label: str):
        entry = widg.QLineEdit()
        entry.setPlaceholderText("-")
        
        self.entries[label] = entry
        
        self.form_layout.addRow(widg.QLabel(label), entry)
        
    def create_combo_box(self, label: str, items: list):
        combo_box = itm.AutocompleteComboBox(items)        
        self.combo_boxes[label] = combo_box
        
        self.form_layout.addRow(widg.QLabel(label), combo_box)
    
    def create_judet_combo(self):
        self.create_combo_box("Judete", judete.keys())
        self.create_combo_box("Localitate", [])
        
        self.combo_boxes["Judete"].currentIndexChanged.connect(self.update_localitate)

    def update_localitate(self):
        selected_judet = self.combo_boxes["Judete"].currentText()
        
        localitati = [localitate["name"] for localitate in judete[selected_judet]]
        
        self.combo_boxes["Localitate"].clear()        
        self.combo_boxes["Localitate"].addItems(localitati)

        is_sector_created: bool = "Sector" in self.combo_boxes
        if buc := selected_judet.lower() == "bucuresti" and not is_sector_created:
            self.create_sector_combo()
        elif is_sector_created:
            self.destroy_sector_combo()
    
    def create_sector_combo(self):
        index = next(row for row in range(self.form_layout.rowCount()) 
                if self.form_layout.itemAt(row, widg.QFormLayout.LabelRole).widget().text() == "Localitate")
        
        combo_box = widg.QComboBox()
        combo_box.addItems([str(i) for i in range(1, 7)])
        
        self.combo_boxes["Sector"] = combo_box
        self.form_layout.insertRow(index + 1, widg.QLabel("Sector"), combo_box)

    def destroy_sector_combo(self):
         index = next(row for row in range(self.form_layout.rowCount()) 
                if self.form_layout.itemAt(row, widg.QFormLayout.LabelRole).widget().text() == "Sector")
         
         self.combo_boxes.pop("Sector")
         self.form_layout.removeRow(index)

    def create_fields(self):
        for data in self.entry_datas:
            match data[0]:
                case "entry":
                    self.create_entry(data[1])
                
                case "combo":
                    if len(data) < 2:
                        raise Exception("not enough data")

                    self.create_combo_box(data[1], data[2])

                case "place":
                    self.create_judet_combo()

                case _:
                    raise Exception(f"Data {data[0]} not implemented")




    
        