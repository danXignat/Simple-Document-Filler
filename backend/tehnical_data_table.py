from docx import Document, table
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os
from icecream import ic

from backend.Table import Table
from config import TEMPLATES_PATH

column_headers = [
        "Denumire",
        "Panou solar",
        "Invertor",
        "Smart Meter",
        "Panou distributie",
        "Sistem prindere",
        "Accesorii"
    ]
    
row_labels = [
        "UM",
        "Cantitate",
        "Putere minima a panoului",
        "Tehnologie panouri",
        "Rama panou",
        "Conectare",
        "Eficienta",
        "Grad protectie",
        "Interval de temper de functionare",
        "Garantie",
        "Garantie eficienta",
        "Putere nominala instalata",
        "MPPT",
        "Iesire",
        "Frecventa",
        "Umiditate max 95%",
        "Serii"
    ]

table = Table(row_labels=row_labels, col_labels=column_headers)

