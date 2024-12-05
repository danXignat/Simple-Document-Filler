import customtkinter as ctk

# Initialize CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Dynamic Summary Example")
        self.geometry("500x400")

        # Step 1: Define StringVars to store data
        self.name_var = ctk.StringVar()
        self.email_var = ctk.StringVar()
        self.phone_var = ctk.StringVar()

        # Step 2: Create the form entries
        self.create_form()
        
        # Step 3: Create the summary page
        self.create_summary()

    def create_form(self):
        """Create input form with Entry widgets."""
        name_entry = ctk.CTkEntry(self, placeholder_text="Salut")
        
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        email_entry = ctk.CTkEntry(self, textvariable=self.email_var)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        phone_entry = ctk.CTkEntry(self, textvariable=self.phone_var)
        phone_entry.grid(row=2, column=1, padx=10, pady=10)

    def create_summary(self):
        """Create the dynamic summary page."""
        ctk.CTkLabel(self, text="Summary:", font=ctk.CTkFont(size=20, weight="bold")).grid(row=3, column=0, pady=20, columnspan=2)

        self.summary_name_label = ctk.CTkLabel(self, textvariable=self.name_var)
        self.summary_name_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.summary_email_label = ctk.CTkLabel(self, textvariable=self.email_var)
        self.summary_email_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.summary_phone_label = ctk.CTkLabel(self, textvariable=self.phone_var)
        self.summary_phone_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()
