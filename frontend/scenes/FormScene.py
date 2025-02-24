import PySide6.QtWidgets as widg
import PySide6.QtCore as core
import PySide6.QtGui as gui

from abc import ABCMeta, ABC, abstractmethod

from config import judete

class FormScene(widg.QWidget):
    def __init__(self, progres_increment: int, parent=None):
        super().__init__(parent)
        self.progres_increment = progres_increment
        self.entry_counter = 0
        self.entries : dict[str, widg.QLineEdit]    = {}
        self.combo_boxes: dict[str, widg.QComboBox] = {}
        
        self.main_layout = widg.QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
       
        self.title = widg.QLabel("Place holder")
        self.main_layout.addWidget(self.title)
       
        # Create a scroll area
        self.scroll_area = widg.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarAsNeeded)

        # Create the form container
        self.form_container = widg.QWidget()
        self.form_layout = widg.QGridLayout(self.form_container)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setVerticalSpacing(10)  # Space between rows
        self.form_layout.setColumnStretch(1, 1)  # Make inputs expand
        
        # Set the form container as the widget for the scroll area
        self.scroll_area.setWidget(self.form_container)
        
        # Add the scroll area to the main layout and have it take available space
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
        self.form_layout.addWidget(widg.QLabel(label), self.entry_counter, 0)
        self.form_layout.addWidget(widg.QLineEdit(), self.entry_counter, 1)
        self.entry_counter+=1
        
    def create_combo_box(self, label: str, items: list):
        combo_box = widg.QComboBox()
        combo_box.addItems(items)
        
        self.form_layout.addWidget(widg.QLabel(label), self.entry_counter, 0)
        self.form_layout.addWidget(combo_box, self.entry_counter, 1)
        self.entry_counter+=1
    
    def create_judet_combo(self):
        judet_combo_box = widg.QComboBox()
        localitate_combo_box = widg.QComboBox()
        
        judet_combo_box.addItems(judete)
        
        judet_combo_box.currentIndexChanged.connect(self.update_localitate)
        
        self.form_layout.addWidget(widg.QLabel("Judet"), self.entry_counter, 0)
        self.form_layout.addWidget(judet_combo_box, self.entry_counter, 1)
        self.combo_boxes["Judet"] = judet_combo_box
        
        self.form_layout.addWidget(widg.QLabel("Localitate"), self.entry_counter + 1, 0)
        self.form_layout.addWidget(localitate_combo_box, self.entry_counter + 1, 1)
        self.combo_boxes["Localitate"] = localitate_combo_box
        
        self.entry_counter += 2
        
    def update_localitate(self):
        selected_judet = self.combo_boxes["Judet"].currentText()
        
        localitati = [localitate["name"] for localitate in judete[selected_judet]]
        
        self.combo_boxes["Localitate"].clear()        
        self.combo_boxes["Localitate"].addItems(localitati)
        