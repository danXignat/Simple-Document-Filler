import PySide6.QtWidgets as widg
import PySide6.QtCore as core
import PySide6.QtGui as gui

class AutocompleteComboBox(widg.QComboBox):
    def __init__(self, items, parent=None, placeholder="-"):
        super().__init__(parent)
        
        # Store the original items
        self.all_items = items
        self.placeholder = placeholder
        self.is_placeholder_visible = True
        
        # Make the combo box editable
        self.setEditable(True)
        # Add all items to the combo box
        self.addItems(items)
        
        # Create a model for the completer
        self.model = core.QStringListModel()
        self.model.setStringList(items)
        
        # Create a proxy model for filtering
        self.proxy_model = core.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(core.Qt.CaseInsensitive)
        
        # Create a custom completer
        self.completer = widg.QCompleter(self.proxy_model, self)
        self.completer.setCompletionMode(widg.QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(core.Qt.CaseInsensitive)
        self.completer.setFilterMode(core.Qt.MatchStartsWith)
        
        # Set the completer for the combo box
        self.setCompleter(self.completer)
        
        # Connect signals
        self.lineEdit().textEdited.connect(self.on_text_edited)
        
        # Set up placeholder
        self.setCurrentIndex(-1)
        self.show_placeholder()
        
        # Connect focus events
        self.lineEdit().installEventFilter(self)
    
    def show_placeholder(self):
        """Show the placeholder text in gray"""
        self.is_placeholder_visible = True
        self.setCurrentText(self.placeholder)
        
        # Style the placeholder text to appear gray
        palette = self.lineEdit().palette()
        palette.setColor(gui.QPalette.Text, gui.QColor(128, 128, 128))  # Gray color
        self.lineEdit().setPalette(palette)
    
    def clear_placeholder(self):
        """Clear the placeholder and reset text color"""
        if self.is_placeholder_visible:
            self.is_placeholder_visible = False
            self.setCurrentText("")
            
            # Reset to default text color
            palette = self.lineEdit().palette()
            palette.setColor(gui.QPalette.Text, gui.QColor(0, 0, 0))  # Black color
            self.lineEdit().setPalette(palette)
    
    def eventFilter(self, obj, event):
        """Handle focus events to manage placeholder behavior"""
        if obj == self.lineEdit():
            if event.type() == core.QEvent.FocusIn:
                # Clear placeholder when gaining focus
                if self.is_placeholder_visible:
                    self.clear_placeholder()
            elif event.type() == core.QEvent.FocusOut:
                # Show placeholder if text is empty and losing focus
                if not self.currentText():
                    self.show_placeholder()
        return super().eventFilter(obj, event)
    
    def on_text_edited(self, text):
        """Update the filter as the user types"""
        # If this is the first edit after showing the placeholder
        if self.is_placeholder_visible:
            self.clear_placeholder()
            # If the user didn't actually type anything (e.g., just clicked), don't filter yet
            if not text:
                return
        
        # Update the filter pattern on the proxy model
        self.proxy_model.setFilterFixedString(text)
        
        # Show the dropdown with matches
        if text and self.proxy_model.rowCount() > 0:
            self.completer.complete()