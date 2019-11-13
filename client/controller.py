import threading

from coms.core import CommunicationManager

URL = 'http://10.0.30.203:8000/python/connect_server.php'

class Controller:
    def __init__(self, interface):
        self._interface = interface
        self._com_manager = CommunicationManager()

    def wait_login(self):
        """Waits for rfid card input and when a card is inputed
        sends a request asking for this student through the communication
        manager if the requests fails asks interface for an error screen"""

        while self._com_manager.get() != '' :
           request = self._com_manager.get_student()

           if request == '' :
                self._interface.text.set_label('Error') # self.get_message() ?
           

        


        raise Exception('Not implemented')

    def request_query(self, table):
        """From a string query changes the display content to the querry
        result."""

        string_query = self._com_manager.get_student._str_


        raise Exception('Not implemented')

    def get_message(self, widget):
        result = self._com_manager.get(URL)
        self._interface.text.set_label(result)


    