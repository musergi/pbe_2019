from py532lib.mifare import Mifare
from pynfc import Nfc, Timeout
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RfidReader:
    def __init__(self):
        """Polls for rfid readers until one is found and it performs
        the adapting work."""

        self._reader = None
        
        for rfid_reader in  [RfidElechousePN532, RfidReader_pn532_i2c, RfidReader_MFRC_RC522]:
            
            try: 
                self._reader = rfid_reader()
                break
            except Exception: 
                print("Failed to open Rfid")

        if self._reader is None:
            raise IOError("Rfid not found")

    def read_uid(self):
        return self._reader.read_uid()

# Add all other rfid readers

class RfidElechousePN532:
	#return uid in hexa str
	def __init__(self):
		self.n = Nfc("pn532_uart:/dev/ttyS0:115200")

	def read_uid(self):
		for card in self.n.poll():
			try:
				uid_hex = card.uid.decode().upper()
				return uid_hex
			except TimeoutException:
				pass

class RfidReader_pn532_i2c:
    def __init__(self):
        self._device = Mifare()
        self._device.SAMconfigure()

    def read_uid(self):
        uid = self._device.scan_field()
        return ''.join('{:02X}'.format(byte) for byte in uid)

class RfidReader_MFRC_RC522:
    def __init__(self):
        self._reader = SimpleMFRC522()

    def read_uid(self):
        id = self._reader.read_id();
        return '%X' % id


if __name__ == "__main__":
    rfid = RfidReader()
    data = rfid.read_uid()
    print(data)