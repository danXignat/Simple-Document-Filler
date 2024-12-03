WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400

LOGO_PATH = "../static/logo.ico"
TEMPLATES_PATH = '../data/template/'
OUTPUT_PATH = "../data/output/"
REGIONS_PATH = "../data/json/regions.json"

COLORS = {
    "green": "#00C48C",  # Green
    "dark_green": "#017d5c",  # Darker green for hover
    
    "blue": "#0095DA",  # Blue
    "light_blue": "#02b4fa",  # Light blue
    "dark_blue" : "#004f6e",
    
    "label_font": ("Verdana", 22, "bold")
}

import json

with open(REGIONS_PATH, 'r') as file:
    judete = json.load(file)
    