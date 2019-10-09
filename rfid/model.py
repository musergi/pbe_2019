from py532lib.mifare import Mifare, MIFARE_SAFE_RETRIES

class RfidReader_pn532_i2c:
    def __init__(self):
        self._device = Mifare()
        self._device.SAMconfigure()
        self._device.set_max_retries(MIFARE_WAIT_FOR_ENTRY)

    def read_uid(self):
        uid = self._device.scan_field()
        return ''.join('{:02X}'.format(byte) for byte in uid)

if __name__ == '__main__':
    rfid = RfidReader_pn532_i2c()
    uid = rfid.read_uid()
    print(uid)
