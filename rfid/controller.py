# System imports
import threading

# Module imports
from model import RfidReader_pn532_i2c

WAITING_UID_TEXT = 'Insert card for uid display'
READ_UID_TEXT = 'Read card with uid {}'

class Controller:
    def __init__(self, window):
        self._window = window

        self._rfid_reader = RfidReader_pn532_i2c()
        self._lock = threading.Lock()

        # Start uid waiter
        self._uid_waiter = threading.Thread(target=self.set_uid, daemon=True)

    def clear_uid(self):
        print('[Controller] - Clearing uid')
        with self._lock:
            self._window.set_label(WAITING_UID_TEXT)

    def set_uid(self):
        print('[Controller] - Setting uid')
        uid = self._rfid_reader.read_uid()
        with self._lock:
            self._window.set_label(READ_UID_TEXT.format(uid))

        # Create another waiter before closing previous
        self._uid_waiter = threading.Thread(target=self.set_uid, daemon=True)


