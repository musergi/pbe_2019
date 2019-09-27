import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

WINDOW_CAPTION = 'Rfid app'

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(self, title=WINDOW_CAPTION)
        self.connect("destroy", Gtk.main_quit)

        self.button = Gtk.Button(label='Click here')
        self.button .connect('clicked', self.button_action)
        self.add(self.button)

    def button_action(self, widget):
        print('Button pressed')

if __name__ == '__main__':
    window = Window()
    window.show()
    Gtk.main()