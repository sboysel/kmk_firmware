import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    # F4 F5 F6 F7 B1 
    col_pins = (
        board.A3,
        board.A2,
        board.A1,
        board.A0,
        board.SCK
    )
    # D4 C6 D7 E6
    row_pins = (
        board.D4,
        board.D5,
        board.D6,
        board.D7
    )
    diode_orientation = DiodeOrientation.COL2ROW
