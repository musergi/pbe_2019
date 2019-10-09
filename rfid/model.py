from py532lib.i2c import Pn532_i2c

class RfidReader_pn532_i2c:
    def __init__(self):
        self.device = Pn532_i2c()
        self.device.SAMconfigure()

    def read_uid(self):
        card_data = self.device.read_mifare().get_data()
        return ''.join('{:02X}'.format(byte) for byte in card_data[-4:])

if __name__ == '__main__':
    rfid = RfidReader_pn532_i2c()
    uid = rfid.read_uid()
    print(uid)
