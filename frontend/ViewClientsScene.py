from ast import Lambda
from typing import List
import customtkinter as ctk
from icecream import ic
from functools import partial

from config import *
from frontend.Scene import Scene
from frontend.DataSummary import DataSummary
from models.SceneType import SceneType

class ClientScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        self.create_label(data_container["Date personale"]["Nume complet"], pady=TITLE_PADY)
        
        self.data_summary = DataSummary(self, self.entries)
        self.data_summary.update_data()
        self.data_summary.pack(padx = 10, pady = 10, fill = "both", expand=True)
             
        self.create_button("Inapoi", self.go_back, side = "left")
        self.create_button("Refoloseste", self.reuse, side = "right")
         
    def go_back(self):
        self.controller.switch_scene("Clienti")
        
    def reuse(self):
        self.controller.reinitialise(self.entries)
        self.controller.switch_scene("Date personale")

class ViewClientsScene(Scene):
    def __init__(self, parent, controller, data_container):
        super().__init__(parent, controller, data_container)
        
        with open(CLIENTS_PATH, 'r') as file:
            self.clients = json.load(file)
        
        self.clients_frame = ctk.CTkScrollableFrame(self, fg_color=self._fg_color, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        self.client_buttons = []
        
        self.create_label("Clienti", pady=TITLE_PADY)
        
        button_frame = ctk.CTkFrame(self, fg_color=self._fg_color)
        for client in self.clients:
            self.create_client_button(client)             
        
        self.create_button("Inapoi", self.go_back, side = "left", parent=button_frame)
        self.create_button("Sterge clientii", self.delete_clients, side = "right", parent=button_frame)
        
        button_frame.pack(padx = 5, pady = 5, side = "bottom", fill = "x")
        self.clients_frame.pack(padx = 10, pady = 10, fill = 'both', expand=True)
        
    def go_back(self):
        self.controller.switch_scene("Meniu principal")
    
    def delete_clients(self):
        for button in self.client_buttons:
            button.destroy()
        self.client_buttons.clear()
        
        with open(CLIENTS_PATH, "r") as file:
            data: List = json.load(file)
        
        data.clear()
        
        with open(CLIENTS_PATH, "w") as file:    
            json.dump(data, file, indent=4)
    
    def create_client_button(self, client):
        button = ctk.CTkButton(
            self.clients_frame,
            text=f"{client["id"]}: {client["name"]}",
            fg_color=COLORS["blue"],
            hover_color=COLORS["dark_blue"],
            command=partial(self.show_client, client["id"], client["data"]),
            font=COLORS["text_font_bold"],
            width=200,
            anchor= "w"
        )
        button.pack(padx = 10, pady = 10)
        
        self.client_buttons.append(button)
            
    def show_client(self, id, data):
        scene = ClientScene(self.controller.scene_container, self.controller, data)
        scene.grid(row=0, column=0, padx = 20, pady = 20, sticky="nsew")
        
        self.controller.scenes[f"Client {id}"] = scene
        
        self.controller.switch_scene(f"Client {id}")
        
    def update_clients(self):
        with open(CLIENTS_PATH, "r") as file:
            data: List = json.load(file)
        
        index = len(self.client_buttons) 
        while len(data) > len(self.client_buttons):
            self.create_client_button(data[index])
            index += 1
            