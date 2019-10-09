from py532lib.mifare import Mifare, MIFARE_SAFE_RETRIES

class RfidReader_pn532_i2c:
    def __init__(self):
        self._device = Mifare()
        self._device.SAMconfigure()
        self._device.set_max_retries(MIFARE_SAFE_RETRIES)

    def read_uid(self):
        uid = self._device.scan_field()
        if not uid:
            raise Exception('Failed to read uid')
        return ''.join('{:02X}'.format(byte) for byte in uid)

if __name__ == '__main__':
    rfid = RfidReader_pn532_i2c()
    uid = rfid.read_uid()
    print(uid)
