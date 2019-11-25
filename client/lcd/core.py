import threading
import math

from . import driver


NUM_COLUMNS = 20

LOGIN_MESSAGE = 'Please login with your university card'
GREATING_MESSAGE = '\nWelcome,\n{}\n'


class LcdManager:
    lcd_lock = threading.Lock()
    lcd_handle = None

    @staticmethod
    def _lcd_init():
        LcdManager.lcd_handle = driver.lcd()

    @staticmethod
    def display_login_message():
        LcdManager.write_autojump(LOGIN_MESSAGE, 2)
    
    @staticmethod
    def display_student_greating(name, surname):
        id_string = name if len(name) + len(surname) + 1 > NUM_COLUMNS else f'{name} {surname}'
        LcdManager.write_multiline(GREATING_MESSAGE.format(_center(id_string)))

    @staticmethod
    def write_autojump(string, start=1):
        words = string.split(' ')
        
        lines = [''] * (start - 1)
        while words:
            line_words = list()
            acc_len = 0
            while words:
                if acc_len + len(words[0]) <= NUM_COLUMNS:
                    acc_len += len(words[0]) + 1
                    line_words.append(words.pop(0))
                else:
                    break
            lines.append(_center(' '.join(line_words)))
            if len(lines) >= 4:
                break
        
        LcdManager.write_multiline('\n'.join(lines))

        

    @staticmethod
    def write_multiline(string):
        with LcdManager.lcd_lock:
            if LcdManager.lcd_handle is None:
                LcdManager._lcd_init()
            LcdManager.lcd_handle.lcd_clear()
            for index, line in enumerate(string.split('\n')):
                LcdManager.lcd_handle.lcd_display_string(line, index + 1)


def _center(string):
    padding_len = NUM_COLUMNS - len(string)
    string_len = padding_len // 2 + len(string)
    return string.rjust(string_len)