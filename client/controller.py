from coms.core import CommunicationManager

URL = 'http://10.0.30.203:8000/python/connect_server.php'

class Controller:
    
    def __init__(self, interface):
        self.interface = interface
        self.cm = CommunicationManager()

    def get_message(self, widget):
        result = self.cm.get(URL)
        self.interface.text.set_label(result)
    