from ctypes import resize
from turtle import width
import customtkinter as ctk
from typing import Dict
import icecream 

from config import COLORS
from models.SceneType import SceneType


class DataSummary(ctk.CTkScrollableFrame):
    def __init__(self, master, data_container):
        super().__init__(master, scrollbar_button_color = COLORS["green"], scrollbar_button_hover_color = COLORS["dark_green"])
        self.data = data_container

        self.series_label_boxes = {"Serii panouri" : [], "Serii invertoare" : [], "Serii Smart Meters" : []}        
        self.series_frames = {"Serii panouri" : None, "Serii invertoare" : None, "Serii Smart Meters" : None}        
        
        self.init_data()
        
        
    def init_data(self):
        for category, subcategories in self.data.items():
            category_name = category if isinstance(category, str) else category.value
            
            self.add_category(category_name, subcategories)
    
    def add_category(self, category_name, subcategories):
        category_label = ctk.CTkLabel(self, text=category_name, font=COLORS["label_font"], text_color=COLORS["blue"])
        category_label.pack(pady=(15, 5), anchor="w")

        collapsible_frame = ctk.CTkFrame(self, corner_radius=10)
        collapsible_frame.pack(fill="x", padx=5, pady=5, anchor="w")
        
        if category_name in self.series_label_boxes.keys():
            self.series_frames[category_name] = collapsible_frame            
        else:
            for row, item in enumerate(subcategories.items()):
                self.add_to_category(collapsible_frame, item, row)
    
    def add_to_category(self, parent_frame, item, row):
        subcategory, value = item
        
        subcategory_title = ctk.CTkLabel(parent_frame, text = subcategory + ':', font=COLORS["text_font"])
        subcategory_title.grid(row = row, column = 0, padx=10, pady=3, sticky="w")
        
        if isinstance(value, int):
            value = str(value)
        
        if isinstance(value, str):
            subcategory_value = ctk.CTkLabel(parent_frame, text = value, font=COLORS["text_font_bold"])
            subcategory_value.grid(row = row, column = 1, padx=10, pady=3, sticky="w")
        else:
            subcategory_value = ctk.CTkLabel(parent_frame, textvariable = value, font=COLORS["text_font_bold"])
            subcategory_value.grid(row = row, column = 1, padx=10, pady=3, sticky="w")
    
    
    def create_series(self, frame, series_count, series_var, row):
        count = ctk.CTkLabel(frame, text = series_count, font=COLORS["text_font"])
        count.grid(row = row, column = 0, padx=10, pady=3, sticky="w")
        
        if isinstance(series_var, int):
            series_var = str(series_var)
        
        if isinstance(series_var, str):
            series = ctk.CTkLabel(frame, text = series_var, font=COLORS["text_font_bold"])
            series.grid(row = row, column = 1, padx=10, pady=3, sticky="w")
        else:
            series = ctk.CTkLabel(frame, textvariable = series_var, font=COLORS["text_font_bold"])
            series.grid(row = row, column = 1, padx=10, pady=3, sticky="w")
            
        return count, series
    
    def update_series(self, category: str):
        frame = self.series_frames[category]
        series_data = self.series_label_boxes[category]
        
        for row, (series_count, series_var) in enumerate(self.data[category].items()):
            if row < len(series_data) and series_data[row][2] is not series_var:
                series_data[row][0].destroy()
                series_data[row][1].destroy()
                
                series_data[row][0], series_data[row][1] = self.create_series(frame, series_count, series_var, row)
                series_data[row][2] = series_var
            else:
                count, series = self.create_series(frame, series_count, series_var, row)
                
                series_data.append(
                    [count, series, series_var]
                )
                
        while len(series_data) > len(self.data[category]):
            series_data[-1][0].destroy()
            series_data[-1][1].destroy()
            series_data.pop()
        
    def update_data(self):
        for category in self.series_label_boxes.keys():
            self.update_series(category)