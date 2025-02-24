from re import S
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                              QStackedWidget, QPushButton, QHBoxLayout)
import PySide6.QtGui as gui
from .scenes.form_scenes import *
from config import WINDOW_HEIGHT, WINDOW_WIDTH

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.scenes = {}
        
        self.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle("Document filler")
        self.setWindowIcon(gui.QIcon("static/logo.ico"))
        self.setup_ui()
        
        
    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        self.stacked_widg = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widg)
        
        self.setup_scenes()
        
    def setup_scenes(self):
        self.main_menu = MainMenuScene()
        self.stacked_widg.addWidget(self.main_menu)
        
        self.main_menu.buttons["Client nou"].clicked.connect(self.new_client)
    
    def back_scene(self):
        back_index: int = self.stacked_widg.currentIndex() - 1
        
        self.stacked_widg.setCurrentIndex(back_index)
    
    def next_scene(self):
        next_index: int = self.stacked_widg.currentIndex() + 1
        
        self.stacked_widg.setCurrentIndex(next_index)
        
    def new_client(self):
        scenes_constr = {
            "Date personale"    : PersonalDataScene,
            "Date implementare" : TargetPlaceScene,
            "Date panouri"      : PanelSelectionScene,
            "Date invertor"     : InvertorSelectionScene,
            "Date Smart Meter"  : SmartMeterSelectionScene,
            "Clienti"           : ViewClientsScene,
            "Rezumat"           : SummaryScene,
        }
        
        progress_increment = 100 // len(scenes_constr)
        for i, (scene_name, scene_class) in enumerate(scenes_constr.items()):
            scene_instance = scene_class(progress_increment * i)
            
            scene_instance.back_btn.clicked.connect(self.back_scene)
            scene_instance.next_btn.clicked.connect(self.next_scene)    
            
            self.stacked_widg.addWidget(scene_instance)
            self.scenes[scene_name] = scene_instance
            
        self.stacked_widg.setCurrentWidget(self.scenes["Date personale"])
        