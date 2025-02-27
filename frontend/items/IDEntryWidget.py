import PySide6.QtWidgets as widg
import PySide6.QtCore as core
import PySide6.QtGui as gui

class IDEntryWidget(widg.QWidget):
    def __init__(self):
        super().__init__()
        
        # Main layout
        self.main_layout = widg.QVBoxLayout(self)
        
        # Create a scroll area for the ID entries
        self.scroll_area = widg.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(core.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarAsNeeded)
        
        # Create a widget to hold the grid layout
        self.scroll_content = widg.QWidget()
        self.scroll_area.setFixedHeight(300)
        self.id_entries_layout = widg.QGridLayout(self.scroll_content)
        
        # Set the content widget to the scroll area
        self.scroll_area.setWidget(self.scroll_content)
        
        # Add scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)
        
        # Buttons layout
        self.buttons_layout = widg.QHBoxLayout()
        self.sterge_button = widg.QPushButton("Sterge")
        self.adauga_button = widg.QPushButton("Adauga")
        self.buttons_layout.addWidget(self.sterge_button)
        self.buttons_layout.addWidget(self.adauga_button)
        self.main_layout.addLayout(self.buttons_layout)
        
        # Connect signals
        self.adauga_button.clicked.connect(self.add_entry)
        self.sterge_button.clicked.connect(self.delete_entry)
        
        # Keep track of current position in the grid
        self.current_row = 0
        self.current_column = 0
        self.entries = []  # List to keep track of added entries

    def add_entry(self):
        # Create a new entry
        entry = widg.QLineEdit()
        entry.setPlaceholderText(f"ID at ({self.current_row}, {self.current_column})")
        
        # Add to the grid at the current position
        self.id_entries_layout.addWidget(entry, self.current_row, self.current_column)
        self.entries.append(entry)
        
        # Update position for next entry
        self.current_column += 1
        if self.current_column > 1:  # Move to next row when we reach column 2
            self.current_column = 0
            self.current_row += 1
            
        # Ensure the newly added widgets are visible by scrolling to them
        self.scroll_area.ensureWidgetVisible(entry)

    def delete_entry(self):
        if not self.entries:
            return
            
        # Remove the last added entry
        entry = self.entries.pop()
        self.id_entries_layout.removeWidget(entry)
        entry.deleteLater()
        
        # Update position pointer
        if self.current_column == 0:
            self.current_column = 1
            self.current_row -= 1
        else:
            self.current_column = 0