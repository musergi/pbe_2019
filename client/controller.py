import threading
import logging

from coms.core import CommunicationManager
from rfid.core import RfidReader

URL = 'http://10.0.30.203:8000/python/connect_server.php'

class Controller:
    def __init__(self, interface):
        self._interface = interface
        self._com_manager = CommunicationManager()
        self._rfid_reader = RfidReader()
        self._student = None
        self.wait_login()

    def wait_login(self):
        """Waits for rfid card input and when a card is inputed
        sends a request asking for this student through the communication
        manager if the requests fails asks interface for an error screen"""
        threading.Thread(target=self._login, daemon=True).start()

    def _login(self):
        while self._student is None:
            uid = self._rfid_reader.read_uid()
            logging.debug(f'Read uid: {uid}')
            self._student = self._com_manager.get_student(uid)
        logging.debug('User logged in')
        self._interface.request_frame('table')

    def request_query(self, table):
        """From a string querry changes the display content to the querry
        result."""
        request_func = lambda: self._do_request(table)
        threading.Thread(target=request_func, daemon=True).start()

    def _do_request(self, table):
        logging.debug(f'Requesting table: {table}')
        csv_table = self._com_manager.get_query(self._student, table, dict())
        self._interface.request_table(table)

    def get_message(self, widget):
        result = self._com_manager.get(URL)
        self._interface.text.set_label(result)


    