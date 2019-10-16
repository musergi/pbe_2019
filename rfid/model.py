from py532lib.mifare import Mifare

class RfidReader_pn532_i2c:
    def __init__(self):
        self._device = Mifare()
        self._device.SAMconfigure()

    def read_uid(self):
        uid = self._device.scan_field()
        return ''.join('{:02X}'.format(byte) for byte in uid)

if __name__ == '__main__':
    rfid = RfidReader_pn532_i2c()
    uid = rfid.read_uid()
    print(uid)
