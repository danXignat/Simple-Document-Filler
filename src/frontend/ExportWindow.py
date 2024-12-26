import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
import threading
import time

import config

class ExportWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        
        top_width = config.EXPORT_WINDOW_HEIGHT  
        top_height = config.EXPORT_WINDOW_WIDTH
        
        x = (screen_width - top_width) // 2
        y = (screen_height - top_height) // 2
        
        self.title("Export in procesare")
        self.iconbitmap(config.LOGO_PATH)
        self.attributes("-topmost", True)
        self.geometry(f"{top_width}x{top_height}+{x}+{y}")
        self.resizable(False, False)
                
        style = ttk.Style()
        style.configure("TProgressbar",
                        thickness=30,             # Set the thickness of the bar
                        length=200,               # Set the length of the progress bar
                        maximum=100,              # Set the maximum value
                        troughcolor="#d3d3d3",    # Set the background color of the trough
                        background=config.COLORS["green"],     # Set the color of the filled part of the bar
                        )
        
        self.progress_bar = ttk.Progressbar(self, style="TProgressbar", orient="horizontal", length=250, mode="determinate")
        self.progress_bar.pack(pady=20)

        self.status_label = tk.Label(self, text="Initializare...")
        self.status_label.pack(pady=10)
        
    def update(self, current, total, file):
        self.progress_bar["value"] = (current / total) * 100
        self.status_label["text"] = f"Exporting {file} ({current}/{total})..."
        self.update_idletasks()
            
    