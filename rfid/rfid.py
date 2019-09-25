from py532lib.i2c import Pn532_i2c

class RfidReader:
    def __init__(self):
        pass

    def read_uid(self):
        return ""

class RfidReaderI2C(RfidReader):
    def __init__(self):
        self.device = Pn532_i2c()
        self.device.SAMconfigure()

    def read_uid(self):
        card_data = self.device.read_mifare().get_data()
        for byte in card_data:
            print(byte)
        return ''.join('{:02x}'.format(x) for x in card_data[1:-1])

if __name__ == '__main__':
    rfid = RfidReaderI2C()
    uid = rfid.read_uid()
    print(uid)