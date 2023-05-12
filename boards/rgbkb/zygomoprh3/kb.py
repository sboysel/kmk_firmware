# assumes Frood CircuitPython
# https://circuitpython.org/board/42keebs_frood/
import board

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

# set side based on drive names
name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP10, board.GP9, board.GP1, board.GP2, board.GP3)
    col_pins = (board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP23)
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.GP17
    data_pin2 = board.GP16
    pixel_pin = board.GP15
