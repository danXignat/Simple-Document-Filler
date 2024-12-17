from enum import Enum, auto
from frontend import *

class SceneType(Enum):
    MainMenu: str = "Meniu principal"
    DocumentsData: str = "Date documente"
    PersonalData: str = "Date personale"
    TargetPlace: str = "Date implementare"
    PanelSelection: str = "Date panouri"
    InvertorSelection: str = "Date invertor"
    SmartMeterSelection: str = "Date Smart Meter"
    Summary: str = "Rezumat"