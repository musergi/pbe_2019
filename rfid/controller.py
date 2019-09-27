from .model import RfidReader_pn532_i2c

class Controller:
    def __init__(self):
        self.rfid_reader = RfidReader_pn532_i2c()

    def clear_uid(self):
        pass

    def set_uid(self):
        pass