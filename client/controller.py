import threading
import logging

import coms
import lcd
from rfid.core import RfidReader, wait_swipe

class Controller:
    def __init__(self, interface):
        self._interface = interface
        self._url = coms.parse.parse_url()
        lcd.core.LcdManager.display_login_message()
        wait_swipe(self.login)
        self._student = None

    def login(self, credentials):
        coms.core.login(self._url + 'login.php', credentials, self.on_login)

    def on_login(self, student):
        self._student = student
        self._interface.request_student(self._student)
        self._interface.request_frame('table')
        lcd.core.LcdManager.display_student_greating(self._student.get_name(), self._student.get_surname())

    def query(self, query):
        coms.core.query(
            self._url + 'query.php',
            {'id':self._student.get_id(), 'query': query},
            self.on_query_response)

    def on_query_response(self, response):
        self._interface.request_table(response)