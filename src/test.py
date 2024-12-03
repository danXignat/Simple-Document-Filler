import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Multi-Page App")
        self.geometry("400x300")
        
        # Container to hold all frames
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)
        
        # Dictionary to manage pages
        self.frames = {}
        
        # Initialize pages
        for PageClass in (HomePage, PageOne, PageTwo):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the initial frame
        self.show_frame("HomePage")
    
    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ctk.CTkLabel(self, text="Home Page", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        ctk.CTkButton(self, text="Go to Page One",
                      command=lambda: controller.show_frame("PageOne")).pack(pady=10)
        ctk.CTkButton(self, text="Go to Page Two",
                      command=lambda: controller.show_frame("PageTwo")).pack(pady=10)


class PageOne(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ctk.CTkLabel(self, text="Page One", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        ctk.CTkButton(self, text="Back to Home",
                      command=lambda: controller.show_frame("HomePage")).pack(pady=10)


class PageTwo(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ctk.CTkLabel(self, text="Page Two", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        ctk.CTkButton(self, text="Back to Home",
                      command=lambda: controller.show_frame("HomePage")).pack(pady=10)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
    
    app = App()
    app.mainloop()
