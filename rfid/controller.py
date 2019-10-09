# System imports
import threading

import gi
from gi.repository import GLib

# Module imports
from model import RfidReader_pn532_i2c


class Controller:
    def __init__(self, window):
        # Init attributes
        self._window = window # Window reference for modifying ui
        self._rfid_reader = RfidReader_pn532_i2c() # Uid reader

        # Start uid waiter
        self._uid_waiter = threading.Thread(target=self.set_uid, daemon=True)
        self._uid_waiter.start()

    def clear_uid(self):
        # If there is not another waiter, create one
        if self._uid_waiter is None:
            self._uid_waiter = threading.Thread(target=self.set_uid, daemon=True)
            self._uid_waiter.start()

    def set_uid(self):
        # Lock thread to read uid
        uid = self._rfid_reader.read_uid()
        
        # Update ui with uid
        GLib.idle_add(self._window.set_uid, uid)

        # Remove thread reference
        self._uid_waiter = None


