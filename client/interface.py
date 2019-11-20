import logging

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk

from controller import Controller

class Interface:
    def __init__(self):
        self._root = Gtk.Window(title='Minerva')
        self._root.connect('destroy', Gtk.main_quit)
        StyleManager.load_styles('main.css')

        self._container = Gtk.Box()
        StyleManager.add_class(self._container, 'main-container')
        self._root.add(self._container)

        self._frames = {
            'login': FrameLogin(self),
            'table': FrameTable(self)
        }
        self._current_frame = None
        self.select_frame('login')

        self._controller = Controller(self) # Init controller

        self._root.show_all()
        logging.debug('Showing interface')

    def select_frame(self, frame_name):
        if self._current_frame is not None:
            self._container.remove(self._current_frame)
        self._current_frame = self._frames[frame_name]
        self._container.add(self._current_frame)
        self._root.show_all()
        logging.debug(f'Selecting frame {frame_name}')

    def set_table(self, csv):
        table = TableRenderer.render_csv(csv)
        self._frames['table'].set_table(table)
        self._root.show_all()
        logging.debug('Table set')

    def request_table(self, csv):
        GLib.idle_add(self.set_table, csv)

    def request_frame(self, frame_name):
        GLib.idle_add(self.select_frame, frame_name)

    def query(self, widget):
        query_str = self._frames['table'].get_entry_text()
        self._controller.request_query(query_str)

    def mainloop(self):
        Gtk.main()


class StyleManager:
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
    @staticmethod
    def render_csv(csv):
        table = Gtk.Grid()

        for num_row, row in enumerate(csv.split('\n')):
            for num_col, col in enumerate(row.split(',')):
                cell_label = Gtk.Label(label=col)
                table.attach(cell_label, num_col, num_row, 1, 1)

        return table


class FrameLogin(Gtk.Box):
    def __init__(self, parent):
        Gtk.Box.__init__(self)
        self._parent = parent

        self._label = Gtk.Label(label='Enter university card to login')
        self.add(self._label)


class FrameTable(Gtk.Box):
    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        self._parent = parent
        
        self._label = Gtk.Label(label='Querry')
        self.add(self._label)

        self._entry = Gtk.Entry()
        self.add(self._entry)

        self._button = Gtk.Button(label='Search')
        self._button.connect('clicked', self._parent.query)
        self.add(self._button)

        self._table = None

    def get_entry_text(self):
        return self._entry['text']

    def set_table(self, table):
        if self._table is not None:
            self.remove(self._table)
        self._table = table
        self.add(self._table)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    interface = Interface()
    interface.mainloop()
