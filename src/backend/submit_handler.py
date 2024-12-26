from tkinter import ttk, messagebox

from backend import parse
from frontend.ExportWindow import ExportWindow

def submit(data, path, export_window):
    parse.parse_documents(data, path, export_window)
    
    export_window.destroy()
    messagebox.showinfo("Info", "Documentele au fost procesate")
    