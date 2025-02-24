from PySide6.QtWidgets import QApplication
from frontend.MainWindow import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(open("ui/style.qss").read())
    
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()