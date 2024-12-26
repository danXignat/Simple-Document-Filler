# from icecream import ic
# from datetime import datetime

# from frontend.Scene import Scene
# from frontend.CalendarEntry import DateEntry
# from frontend.BackNext import BackNext
# from models.SceneType import SceneType
# from config import *

class DocumentsDataScene:
    pass

# class DocumentsDataScene(Scene):
#     def __init__(self, parent, controller, data_container):
#         super().__init__(parent, controller, data_container)
#         self.entries[SceneType.DocumentsData] = {}
#         self.local_entries = self.entries[SceneType.DocumentsData]
#         self.combo_boxes = {}
        
#         self.create_label("Date documente", pady=TITLE_PADY)
        
#         self.calendar = DateEntry(self, "Data intocmire", self._fg_color)
#         self.calendar.pack(pady=10)
        
#         self.local_entries["Data intocmire"] = self.calendar.string_var
        
#         self.bacl_next = BackNext(self, self.go_back, self.submit, self._fg_color)
        
#     def go_back(self):
#         self.controller.switch_scene(SceneType.MainMenu)
    
#     def submit(self):
#         self.controller.switch_scene(SceneType.PersonalData)
    