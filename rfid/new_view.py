# Third party imports
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from controller import Controller


WINDOW_CAPTION = 'rfid_gtk'
DEFAULT_LABEL_CONTENT = 'Please login with your university card'
UID_LABEL_CONTENT = 'UID: {}'
DEFAULT_BUTTON_CONTENT = 'Clear'


class Window:
    def __init__(self)
        self._window = Gtk.Window(title=WINDOW_CAPTION)
        self._window.connect('destroy', Gtk.main_quit)

        self._container = Gtk.Box(orientation=Gtk.Orentation.VERTICAL, spacing=8)
        self._window.add(self._container)

        self._label = Gtk.Label(label=DEFAULT_LABEL_CONTENT)
        self._container.pack_end(self._label, True, True, 0)

        self._button = Gtk.Button(label=DEFAULT_BUTTON_CONTENT)
        self._button.connect('clicked', self.clear_uid)
        self._container.pack_end(self._button, True, False, 0)

        self._ctl = Controller(self)

        self._window.show_all()

    def clear_uid(self, widget):
        self._ctl.clear_uid()
        self._label.set_label(DEFAULT_LABEL_CONTENT)

    def set_uid(self, uid):
        # Set appropiated text into the label
        self._label.set_label(UID_LABEL_CONTENT.format(uid))


if __name__ == '__main__':
    win = Window()
    Gtk.main()