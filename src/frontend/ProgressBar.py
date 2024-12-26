import customtkinter as ctk
from PIL import Image, ImageTk
from config import *

class ProgressBar(ctk.CTkFrame):
    def __init__(self, master, n, current_progress, fg_color, width=200, height=150):
        super().__init__(master, fg_color=fg_color)
       
        self.n = n
        self.k = 100 / n
        self.progress = current_progress / self.n 
        
        self.width = width
        self.height = height
        
        self.setup_progress_bar()
        self.setup_icon()
        
    def setup_progress_bar(self):
        self.progress_bar = ctk.CTkProgressBar(
            self, 
            width=self.width,
            height=20,
            progress_color=COLORS["dark_green"]
        )
        self.progress_bar.grid(row=0, column=0, pady=5)
        self.progress_bar.set(self.progress)
        
    def setup_icon(self):
        image = Image.open(LOGO_PATH).convert("RGBA")
        
        self.icon_image = ctk.CTkImage(light_image=image, dark_image=image)
        
        self.icon_label = ctk.CTkLabel(
            self,
            text="",  # No text, only image
            image=self.icon_image,
            height=20,
            fg_color=COLORS["dark_green"]
        )
        
        self.icon_label.place(x=(self.progress * self.width - 8)*0.90, y=5)
        
    def increase(self):
        if self.progress + self.k > 100:
            return 
        
        self.progress += self.k
        self.progress_bar.set(self.progress / 100)
        
        new_x = (self.progress/100 * self.width - 8)*0.92
        self.icon_label.place(x=new_x, y=5)