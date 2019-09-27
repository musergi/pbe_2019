import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

WINDOW_CAPTION = 'Rfid app'

CLEAR_BUTTON_TEXT = 'Click to clear'
WAITING_UID_TEXT = 'Insert card for uid display'
READ_UID_TEXT = 'Read card with uid {}'

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=WINDOW_CAPTION)
        self.connect("destroy", Gtk.main_quit)

        self.label = Gtk.Label(label=WAITING_UID_TEXT)
        self.add(self.label)

        self.button = Gtk.Button(label=CLEAR_BUTTON_TEXT)
        self.button .connect('clicked', self.button_action)
        self.add(self.button)

    def button_action(self, widget):
        print('Button pressed')

if __name__ == '__main__':
    window = Window()
    window.show_all()
    Gtk.main()