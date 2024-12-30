import customtkinter as ctk
from frontend.App import App
from backend.request_admin import request_admin    
    
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    # request_admin()
    
    app = App()
    app.mainloop()

