import customtkinter as ctk

from config import COLORS
from models.SceneType import SceneType

import icecream

class DataSummary(ctk.CTkScrollableFrame):
    def __init__(self, master, data_container):
        super().__init__(master, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        
        self.data = data_container

        self.init_data()
        
        self.panel_labels = {}
        
    def init_data(self):
        for category, subcategories in self.data.items():
            category_name = category if isinstance(category, str) else category.value
            
            self.add_category(category_name, subcategories)
        
    def add_panels(self):
        for i, (label, panou) in enumerate(self.data["Panouri"].items()):
            if label not in self.panel_labels:
                subcategory_title = ctk.CTkLabel(self.panel_frame, text = label + ':', font=("Verdana", 14))
                subcategory_title.grid(row = i, column = 0, padx=10, pady=3, sticky="w")
                
                subcategory_value = ctk.CTkLabel(self.panel_frame, textvariable = panou, font=("Verdana", 14, "bold"))
                subcategory_value.grid(row = i, column = 1, padx=10, pady=3, sticky="w")
                
                self.panel_labels.update({label: (subcategory_title, subcategory_value)})
    
    def delete_panels(self):
        while (len(self.panel_labels) > len(self.data["Panouri"].items())):
            label, (label_obj, panel) = self.panel_labels.popitem()
            
            label_obj.destroy()
            panel.destroy()
    
    def update_data(self):
        if(len(self.data["Panouri"].items()) > len(self.panel_labels)):
            self.add_panels()
        else:
            self.delete_panels()
    
    def add_category(self, category_name, subcategories):
        category_label = ctk.CTkLabel(self, text=category_name, font=("Verdana", 22, "bold"), text_color=COLORS["blue"])
        category_label.pack(pady=(15, 5), anchor="w")

        collapsible_frame = ctk.CTkFrame(self, corner_radius=10)
        collapsible_frame.pack(fill="x", padx=5, pady=5, anchor="w")
        
        if category_name == "Panouri":
            self.panel_frame = collapsible_frame
        
        for row, item in enumerate(subcategories.items()):
            self.add_to_category(collapsible_frame, item, row)
            
    
    def add_to_category(self, parent_frame, item, row):
        subcategory, value = item
        
        subcategory_title = ctk.CTkLabel(parent_frame, text = subcategory + ':', font=("Verdana", 14))
        subcategory_title.grid(row = row, column = 0, padx=10, pady=3, sticky="w")
        
        subcategory_value = ctk.CTkLabel(parent_frame, textvariable = value, font=("Verdana", 14, "bold"))
        subcategory_value.grid(row = row, column = 1, padx=10, pady=3, sticky="w")