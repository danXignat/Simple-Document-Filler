import customtkinter as ctk
from tkcalendar import DateEntry
import tkinter.ttk as ttk

from config import COLORS
from frontend.Signal import Signal

class CalendarEntry(DateEntry):
    def __init__(self, master):
        style = ttk.Style()
        style.theme_use('clam') 
        
        style.configure( 'custom.DateEntry', 
                fieldbackground=COLORS["blue"],
                foreground='white',   
                background=COLORS["green"], 
                arrowcolor='white',   
                bordercolor=COLORS["blue"],
            )    
        
        style.map("custom.DateEntry",
          foreground=[('active', 'white')],
          background=[('active', COLORS["dark_green"])])
        
        super().__init__(master,
                placeholder="Data intocmire",
                background=COLORS["green"],
                foreground="white",
                width=0,
                style = 'custom.DateEntry',
                font=("Arial", 0),
                date_pattern="dd-mm-yyyy",
                locale = 'ro_RO'
            )
        
class DateEntry(ctk.CTkFrame):
    def __init__(self, master, label, fg_color):
        super().__init__(master, fg_color=fg_color)
        self.pack(pady=10, anchor = 'center')
        
        self.update_signal = Signal()
        self.label = label
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.string_var = ctk.StringVar(value = label)
        
        self.date_label = ctk.CTkLabel(self, textvariable = self.string_var, corner_radius=10, fg_color=COLORS["blue"], font=COLORS["text_font_bold"])
        self.date_label.grid(row = 0, column = 0, sticky="e", padx = 5, pady = 0)
        
        self.calendar = CalendarEntry(self)
        self.calendar.bind("<<DateEntrySelected>>", lambda event : self.update_date())
        self.calendar.grid(row = 0, column = 1, sticky="w", padx = 5, pady = 0)
        
        self.date_label = ctk.CTkButton(self, text="Selecteaza data", command=lambda : self.calendar.drop_down(),  fg_color=COLORS["green"], hover_color=COLORS["dark_green"], font=COLORS["text_font"])
        self.date_label.grid(row = 0, column = 1, sticky="w", padx = 5, pady = 0)
        
    def update_date(self):
        date = self.calendar.get_date()
        
        formatted_date = date.strftime("%d-%m-%Y")
        
        self.string_var.set(formatted_date)
        
        self.update_signal.emit(self.label, date)
        