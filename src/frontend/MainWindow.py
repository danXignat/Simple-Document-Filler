from tkinter import (
    Tk, Label, Entry, Button, filedialog,
    IntVar, messagebox, Frame, Canvas, Scrollbar, PhotoImage
)
from typing import Any, Dict
from config import LOGO_PATH, OUTPUT_PATH

from backend import word

class MainWindow:
    labels = [
            "Nume", "Data",
            "Judet", "NrStrada",
            "CNP", "SeriaCi",
            "NrCi", "Strada", "CodPostal",
            "NumarTelefon", "Email"
    ]
    
    root = Tk()
    
    data_entries  = []
    panel_entries = []
    
    def __init__(self):
        self.root.title("")
        self.root.iconphoto(True, PhotoImage(file=LOGO_PATH))

        # General information fields
        for i, label in enumerate(self.labels):
            Label(self.root, text=label).grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = Entry(self.root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.data_entries.append(entry)

        # Field for the number of panels
        self.panel_count_var = IntVar()
        Label(self.root, text="Number of Panels").grid(row=len(self.labels), column=0, padx=5, pady=5, sticky='e')
        panel_count_entry = Entry(self.root, textvariable=self.panel_count_var)
        panel_count_entry.grid(row=len(self.labels), column=1, padx=5, pady=5)

        # Panel fields frame
        self.panel_frame = Frame(self.root)
        self.panel_frame.grid(row=len(self.labels) + 2, column=0, columnspan=2, pady=10)

        # Set Panel Count button
        Button(self.root, text="Numar panouri", 
               command=self._update_panel_fields).grid(row=len(self.labels) + 1, column=1, pady=10)

        # Submit button
        Button(self.root, text="Genereaza", 
               command=lambda : word.submit(*self._generate_data())).grid(row=len(self.labels) + 3, column=1, pady=10)

    def run(self):
        self.root.mainloop()
    
    def get_data(self) -> Dict[str, Any]:
        data = {label : entry.get() for label, entry in zip(self.labels, self.data_entries)}
        
        data.update(
            { "panouri" : [serie.get() for serie in self.panel_entries] }
        )
        
        print(data)
        
        return data
    
    def _generate_data(self):
        default_path = OUTPUT_PATH
        save_folder = filedialog.askdirectory(title="Selecteaza folderul", initialdir=default_path)
        if not save_folder:
            print("Niciun folder selectat")
        
        return self.get_data(), save_folder + '/'        
    
    def _update_panel_fields(self):
        """Update panel fields dynamically based on the panel count."""
        try:
            count = int(self.panel_count_var.get())
            if count < 1:
                raise ValueError("Numarul de panouri trebuie sa fie macar 1.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Introdu un numar valid de panouri")
            return

        # Clear existing panel fields
        for widget in self.panel_frame.winfo_children():
            widget.destroy()

        # Add new fields for each panel's code
        for i in range(count):
            Label(self.panel_frame, text=f"Panou {i + 1}").grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = Entry(self.panel_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.panel_entries.append(entry)