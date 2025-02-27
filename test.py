from PySide6.QtWidgets import QApplication, QScrollArea, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel

app = QApplication([])

# Create the scroll area
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)  # Important to make the scroll area resize its widget

# Create a container widget to hold all your layouts
container = QWidget()

# Create a main layout for the container
main_layout = QVBoxLayout(container)

# First layout (vertical)
layout1 = QVBoxLayout()
layout1.addWidget(QLabel("Layout 1 - Vertical"))
for i in range(5):
    layout1.addWidget(QPushButton(f"Button {i+1}"))

# Second layout (horizontal)
layout2 = QHBoxLayout()
layout2.addWidget(QLabel("Layout 2 - Horizontal"))
for i in range(3):
    layout2.addWidget(QPushButton(f"Button {i+1}"))

# Add both layouts to the main layout
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)

# Set the container as the scroll area's widget
scroll_area.setWidget(container)

# Show the scroll area
scroll_area.resize(300, 200)
scroll_area.show()

app.exec_()