"""
All interface components are included in this file.
"""
import logging

# GUI library import
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk

from controller import Controller # Controller class import


GREATING_MESSAGE = 'Welcome, {}'


class Interface:
    """Parent class of all other interface classes.
    This class is in charge of interacting with the controller. It is also
    in charge of changing between the diferent frames of our interface.
    The methods that start with request are thread-safe."""
    def __init__(self):
        # Init window widget
        self._root = Gtk.Window(title='Minerva')
        self._root.connect('destroy', Gtk.main_quit)

        # Load css
        StyleManager.load_styles('main.css')

        # Main container
        self._container = Gtk.Stack()
        StyleManager.add_class(self._container, 'main-container')
        self._root.add(self._container)

        # Create all frames
        self._frames = {
            'login': FrameLogin(self),
            'table': FrameTable(self)
        }
        for name, frame in self._frames.items():
            self._container.add_named(frame, name)
        self.select_frame('login')

        # Init controller
        self._controller = Controller(self) # Init controller

        # Show interface
        self._root.show_all()
        logging.debug('Showing interface')

        # Wait for user login
        self._controller.wait_login()

    def select_frame(self, frame_name):
        """Makes visible the frame with the specified name.
        If a frame is already displaying removes it, then sets
        the asked frame to current_frame and adds it to the main
        container. Finally redraws the display."""
        self._container.set_visible_child_name(frame_name)
        logging.debug(f'Selecting frame {frame_name}')

    def set_table(self, csv):
        """Sets the table in the table frame."""
        table = TableRenderer.render_csv(csv)
        self._frames['table'].set_table(table)
        self._root.show_all()
        logging.debug('Table set')

    def set_student(self, student):
        self._frames['table'].set_student(student)

    def request_table(self, csv):
        """Thread safe version of set_table"""
        GLib.idle_add(self.set_table, csv)

    def request_frame(self, frame_name):
        """Thread safe version of select_frame"""
        GLib.idle_add(self.select_frame, frame_name)

    def request_student(self, student):
        GLib.idle_add(self.set_student, student)

    def query(self, widget):
        """Asks the controller for a table"""
        query_str = self._frames['table'].get_entry_text()
        self._controller.request_query(query_str)

    def mainloop(self):
        """Starts the interface loop"""
        Gtk.main()


class StyleManager:
    """Class wraping all style related methods."""
    @staticmethod
    def load_styles(source_filepath):
        css_data = ''

        with open(source_filepath, 'r') as f:
            css_data = f.read().encode('ascii', 'ignore')

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css_data)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    
    @staticmethod
    def add_class(widget, class_name):
        context = widget.get_style_context()
        context.add_class(class_name)


class TableRenderer:
    """Class that renders tables"""
    @staticmethod
    def render_csv(csv):
        table = Gtk.Grid()

        for num_row, row in enumerate(csv.split('\n')):
            for num_col, col in enumerate(row.split(',')):
                if num_row == 0:
                    col = col.capitalize()
                cell_label = Gtk.Label(label=col)
                StyleManager.add_class(cell_label, 'table-element')
                table.attach(cell_label, num_col, num_row, 1, 1)

        return table


class FrameLogin(Gtk.Box):
    """Frame shown while logging in"""
    def __init__(self, parent):
        Gtk.Box.__init__(self)
        self._parent = parent

        self._label = Gtk.Label(label='Enter university card to login')
        self.add(self._label)


class FrameTable(Gtk.Grid):
    """Frame use for searching the database"""
    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        self._parent = parent
        
        self._name_label = Gtk.Label()
        StyleManager.add_class(self._name_label, 'small-font')
        self.attach(self._name_label, 3, 0, 1, 1)

        self._label = Gtk.Label(label='Query')
        StyleManager.add_class(self._label, 'vertical-spacing')
        self.attach(self._label, 0, 1, 1, 1)

        self._entry = Gtk.Entry()
        self.attach(self._entry, 0, 2, 2, 1)

        self._button = Gtk.Button(label='Search')
        self._button.connect('clicked', self._parent.query)
        self.attach(self._button, 2, 2, 1, 1)

        self._table = None

    def get_entry_text(self):
        return self._entry.get_text()

    def set_table(self, table):
        if self._table is not None:
            self.remove(self._table)
        self._table = table
        self.attach(self._table, 0, 3, 4, 1)

    def set_student(self, student):
        logging.debug('Setting student name')
        self._name_label.set_label(GREATING_MESSAGE.format(student.get_name()))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    interface = Interface()
    interface.mainloop()
