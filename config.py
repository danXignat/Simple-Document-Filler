import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


WINDOW_HEIGHT = 850
WINDOW_WIDTH = 550

EXPORT_WINDOW_HEIGHT = 500
EXPORT_WINDOW_WIDTH = 150

LOGO_PNG_PATH = resource_path("static\\logo_png.png")
LOGO_PATH = resource_path("static\\logo.ico")
TEMPLATES_PATH = resource_path('data\\template\\')
OUTPUT_PATH = resource_path("data\\output\\")

REGIONS_PATH = resource_path("data\\json\\regions.json")
INVERTORS_PATH = resource_path("data\\json\\invertors.json")
PANELS_PATH = resource_path("data\\json\\panels.json")
SMART_METER_PATH = resource_path("data\\json\\smartmeter.json")
CLIENTS_PATH = resource_path("data\\json\\clients.json")
DEFAULT_DATA = resource_path("data\\json\\default_data.json")

BOX_WIDTH = 400
TITLE_PADY = 30
COLORS = {
    "green": "#00C48C",  # Green
    "dark_green": "#017d5c",  # Darker green for hover
    
    "blue": "#0095DA",  # Blue
    "light_blue": "#02b4fa",  # Light blue
    "dark_blue" : "#004f6e",
    
    "redish" : "#F45463",#a12a35
    "redish_dark" : "#a12a35",
    
    "label_font": ("Verdana", 22, "bold"),
    "text_font_bold" : ("Verdana", 14, "bold"),
    "text_font" : ("Verdana", 14)
}

import json

with open(REGIONS_PATH, 'r') as file:
    judete = json.load(file)
    
with open(INVERTORS_PATH, 'r') as file:
    invertors = json.load(file)
    
with open(PANELS_PATH, 'r') as file:
    panels = json.load(file)
    
with open(SMART_METER_PATH, 'r') as file:
    smart_meters = json.load(file)
    