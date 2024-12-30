import customtkinter as ctk

from frontend.Scene import Scene
from models.SceneType import SceneType
from config import COLORS


class MainMenuScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.buttons_frame = ctk.CTkFrame(self, fg_color=self._fg_color)
        self.buttons_frame.pack(expand = True)
        
        self.create_button("Client nou", self.new_client_scene, pady = 20, parent = self.buttons_frame)
        self.create_button("Vezi clienti", self.view_clients_scene, pady = 20, parent = self.buttons_frame)

    def new_client_scene(self):
        self.controller.switch_scene("Date personale")

    def view_clients_scene(self):
        self.controller.switch_scene("Clienti")