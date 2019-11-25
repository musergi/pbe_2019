import threading
import logging

import coms
import lcd
from rfid.core import RfidReader

class Controller:
    def __init__(self, interface):
        self._interface = interface
        self._rfid_reader = RfidReader()
        self._student = None

    def wait_login(self):
        """Waits for rfid card input and when a card is inputed
        sends a request asking for this student through the communication
        manager if the requests fails asks interface for an error screen"""
        threading.Thread(target=self._login, daemon=True).start()

    def _login(self):
        lcd.core.LcdManager.display_login_message()
        while self._student is None:
            uid = self._rfid_reader.read_uid()
            logging.debug(f'Read uid: {uid}')
            self._student = coms.core.get_student(uid)
        logging.debug('User logged in')
        self._interface.request_student(self._student)
        self._interface.request_frame('table')
        lcd.core.LcdManager.display_student_greating(self._student.get_name(), self._student.get_surname())

    def request_query(self, query_str):
        """From a string querry changes the display content to the querry
        result."""
        request_func = lambda: self._do_request(query_str)
        threading.Thread(target=request_func, daemon=True).start()

    def _do_request(self, query_str):
        logging.debug(f'Requesting table: {query_str}')
        table, param_dict = coms.parse.str_to_params(query_str)
        csv_table = coms.core.get_query(self._student, table, param_dict)
        logging.debug(f'Response table: \n{csv_table}')
        self._interface.request_table(csv_table)