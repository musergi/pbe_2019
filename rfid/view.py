# Third party imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Module imports
from controller import Controller, WAITING_UID_TEXT

# Constants
WINDOW_CAPTION = 'Rfid app'

CLEAR_BUTTON_TEXT = 'Click to clear'


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=WINDOW_CAPTION)
        self.connect("destroy", Gtk.main_quit)

        self.style_manager = StyleManager()

        # Create grid layout
        self.grid_layout = Gtk.Grid()
        self.add(self.grid_layout)

        # Add label
        self.label = Gtk.Label(label=WAITING_UID_TEXT)
        self.grid_layout.attach(self.label, 0, 0, 1, 1)

        # Add button
        self.button = Gtk.Button(label=CLEAR_BUTTON_TEXT)
        self.button.connect('clicked', self.button_action)
        self.grid_layout.attach(self.button, 0, 1, 1, 1)

        # Set-up controller
        self.ctl = Controller(self)

    def button_action(self, widget):
        self.ctl.clear_uid()

    def set_label(self, text):
        self.label.set_label(text)



class StyleManager:
    def __init__(self):
        css_string = ""

        with open('main.css') as file:
            css_string = file.read().encode('ascii', 'ignore')

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css_string)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__ == '__main__':
    window = Window()
    window.show_all()
    Gtk.main()