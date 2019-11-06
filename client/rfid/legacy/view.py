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
    """Class in charge of creating the graphical interface. Creates all the
    necessary PyGObject widgets for our interface. It has the 2 methods used
    for changing the main label between its 2 states."""
    def __init__(self):
        """Window constructor, in this method all the interface is build and
        the main label set to it initial state."""
        self._window = Gtk.Window(title=WINDOW_CAPTION)
        self._window.connect('destroy', Gtk.main_quit)

        self._style_manager = StyleManager()

        self._container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self._window.add(self._container)

        self._label = Gtk.Label(label=DEFAULT_LABEL_CONTENT)
        label_context = self._label.get_style_context()
        label_context.add_class('main-label')
        label_context.add_class('green-background')
        self._container.pack_start(self._label, True, True, 0)

        self._button = Gtk.Button(label=DEFAULT_BUTTON_CONTENT)
        self._button.connect('clicked', self.clear_uid)
        self._container.pack_start(self._button, True, False, 0)

        self._ctl = Controller(self)

        self._window.show_all()

    def clear_uid(self, widget):
        """Sets the label content to its default and if changed returns to
        the default styling."""
        self._ctl.clear_uid()
        self._label.set_label(DEFAULT_LABEL_CONTENT)

        label_context = self._label.get_style_context()
        if not label_context.has_class('green-background'):
            label_context.remove_class('red-background')
            label_context.add_class('green-background')

    def set_uid(self, uid):
        """Sets the uid display message to the specified and changes the
        styling."""
        self._label.set_label(UID_LABEL_CONTENT.format(uid))

        label_context = self._label.get_style_context()
        if not label_context.has_class('red-background'):
            label_context.remove_class('green-background')
            label_context.add_class('red-background')



class StyleManager:
    """Class in charge of creating the styling context and loading the
    css styling from a file."""
    def __init__(self):
        css_string = ''

        with open('main.css', 'r') as f:
            css_string = f.read().encode('ascii', 'ignore')

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css_string)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__ == '__main__':
    win = Window()
    Gtk.main()