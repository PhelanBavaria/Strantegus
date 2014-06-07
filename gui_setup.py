

from gui.gui import GUI
from gui.widgets import Button


gui = GUI()
test_button = Button(gui, (100, 100))
test_button.on_left_click = gui.quit