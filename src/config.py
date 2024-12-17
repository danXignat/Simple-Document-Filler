WINDOW_HEIGHT = 800
WINDOW_WIDTH = 550

LOGO_PATH = "../static/logo.ico"
TEMPLATES_PATH = '../data/template/'
OUTPUT_PATH = "../data/output/"
REGIONS_PATH = "../data/json/regions.json"
INVERTORS_PATH = "../data/json/invertors.json"
PANELS_PATH = "../data/json/panels.json"
SMART_METER_PATH = "../data/json/smartmeter.json"

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
    