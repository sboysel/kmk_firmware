import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP28,
        board.GP27,
        board.GP18,
        board.GP17,
        board.GP14,
        board.GP0,
        board.GP3,
        board.GP5,
        board.GP10,
        board.GP12,
    )
    row_pins = (
        board.GP7,
        board.GP9,
        board.GP22,
        board.GP20,
    )
    diode_orientation = DiodeOrientation.COL2ROW
