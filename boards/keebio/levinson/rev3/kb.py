# assumes Frood CircuitPython
# https://circuitpython.org/board/42keebs_frood/
import board

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

# set side based on drive names
name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

row_pins_left = (board.D4, board.D7, board.D8, board.D9)
col_pins_left = (board.TX, board.D29, board.D26, board.SCK, board.MISO, board.MOSI)
row_pins_right = (board.D4, board.MOSI, board.MISO, board.SCK)
col_pins_right = (board.D29, board.D26, board.TX, board.D9, board.D8, board.D7)

class KMKKeyboard(_KMKKeyboard):
    row_pins = row_pins_right if isRight else row_pins_left
    col_pins = col_pins_right if isRight else col_pins_left
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.D3
    coord_mapping = [
        0,  1,  2,  3,  4,  5,      29, 28, 27, 26, 25, 24, 
        6,  7,  8,  9, 10, 11,      35, 34, 33, 32, 31, 30,
       12, 13, 14, 15, 16, 17,      41, 40, 39, 38, 37, 36,
       18, 19, 20, 21, 22, 23,      47, 46, 45, 44, 43, 42
    ]
