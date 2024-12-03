from turtle import window_width
import customtkinter as ctk
from PIL import Image, ImageTk

from config import *

from frontend import *
from models.SceneType import SceneType

scenes_constr = {
    SceneType.MainMenu : MainMenuScene,
    SceneType.PersonalData : PersonalDataScene,
    SceneType.TargetPlace : TargetPlaceScene
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
        
        self.scenes = {}
        
        for scene_type, scene_class in scenes_constr.items():
            scene = scene_class(parent=self.scene_container, controller=self)
            self.scenes[scene_type] = scene
            
            scene.grid(row=0, column=0, padx = 20, pady = 20, sticky="nsew")
            
        
        self.switch_scene(SceneType.MainMenu)
    
    def switch_scene(self, scene_type: SceneType):
        """Switch to a different scene."""
        scene = self.scenes[scene_type]
        scene.tkraise()

