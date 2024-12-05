from turtle import window_width
import customtkinter as ctk
from PIL import Image, ImageTk

from config import *
from frontend import *
from models.SceneType import SceneType

scenes_constr = {
    SceneType.MainMenu : MainMenuScene,
    SceneType.PersonalData : PersonalDataScene,
    SceneType.TargetPlace : TargetPlaceScene,
    SceneType.PanelSelection : PanelSelectionScene,
    SceneType.InvertorSelection : InvertorSelectionScene,
    SceneType.SmartMeterSelection : SmartMeterSelectionScene,
    SceneType.Summary : SummaryScene
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.iconbitmap(LOGO_PATH)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.scene_container = ctk.CTkFrame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, corner_radius=0)
        self.scene_container.grid(row=0, column=0, sticky="nsew")
        
        self.scene_container.grid_rowconfigure(0, weight=1)
        self.scene_container.grid_columnconfigure(0, weight=1)
        
        self.data_container = {}
        self.scenes = {}
        
        self.init_scenes()
    
        self.switch_scene(SceneType.MainMenu)
        
    def init_scenes(self):
        for scene_type, SceneClass in scenes_constr.items():
            scene = SceneClass(
                parent=self.scene_container,
                controller=self,
                data_container = self.data_container
                )
            
            self.scenes[scene_type] = scene
            
            scene.grid(row=0, column=0, padx = 20, pady = 20, sticky="nsew")

    def switch_scene(self, scene_type: SceneType):
        """Switch to a different scene."""
        scene = self.scenes[scene_type]
        
        if isinstance(scene, SummaryScene):
            scene.update_data()
        
        scene.tkraise()

