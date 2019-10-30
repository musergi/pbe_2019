import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from controller import Controller


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Client")
        self.set_border_width(6)
        self.set_default_size(500, 100)
        self.set_name("main_window")

        self.ctl = Controller(self)

        #create box

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        hbox.set_homogeneous(False)
        self.add(hbox)

        #text view
        
        self.text = Gtk.Label()
        self.text.set_property("width-request", 180)
        self.text.set_property("height-request", 180)
        self.text.set_justification(Gtk.Justification.FILL)
        self.text.set_wrap_mode(True)
        self.text.set_monospace(True)
        self.text.set_name("text_style")

        #add text

        hbox.pack_start(self.text, True, True, 0)

        #action button

        self.display_button = Gtk.Button(label="Request")
        self.display_button.set_property("width-request", 30)
        self.display_button.set_property("height-request", 10)
        self.display_button.connect("clicked", self.ctl.get_message)
        self.display_button.set_name("action_button")

        #add action button to box

        hbox.pack_start(self.action_button, True, True, 0)
        
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()


        

    # def display(self, widget):
    #     LcdObject = I2C_LCD_driver.lcd()
    #     LcdObject.lcd_clear()
    #     buffer = self.texting.get_buffer()
    #     start_it = buffer.get_start_iter()
    #     end_it = buffer.get_end_iter()
    #     string = buffer.get_text(start_it, end_it, False)
    #     self.lcd.write_lines(string.split('\n'))
    #     time.sleep(1)
    #     buffer.delete(start_it, end_it)

def main():
    def gtk_style():

        data = ''
        with open('client.css') as f:
            data = f.read().encode('ascii', 'ignore')
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(data)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    gtk_style()
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()

