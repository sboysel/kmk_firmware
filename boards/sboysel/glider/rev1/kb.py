import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP6,
        board.GP5,
        board.GP4,
        board.GP3,
        board.GP2,
        board.A3,
        board.GP28,
        board.GP27,
        board.GP22,
        board.GP21,
    )
    row_pins = (
        board.GP14,
        board.GP15,
        board.GP17,
        board.GP16,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    rgb_pixel_pin = board.GP25
    tap_time = 200
