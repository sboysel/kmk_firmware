import board

from kb import KMKKeyboard, isRight
keyboard = KMKKeyboard()

from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False,
    split_target_left=not isRight,
    uart_flip=False,
    data_pin=board.GP9,  # RX
    data_pin2=board.GP8, # TX
    use_pio=True,
)
keyboard.modules.append(split)

# === layer tap ---------------------------------------------------------------
keyboard.tap_time = 200
# NAV (layer 1)
LT_SPC = KC.LT(1, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# FUN (layer 2)
LT_TAB = KC.LT(2, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# SYM (layer 3)
LT_ENT = KC.LT(3, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# NUM (layer 4)
LT_BSPC = KC.LT(4, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)

# === home row mods ------------------------------------------------------------
MT_A = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_S = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_D = KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)

MT_J = KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_K = KC.MT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_L = KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_QUOT = KC.MT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)

# === keymap -------------------------------------------------------------------
keyboard.keymap = [
    # BASE
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        MT_A,    MT_S,    MT_D,    MT_F,    KC.G,    KC.H,    MT_J,    MT_K,    MT_L,    MT_QUOT,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
                          KC.ESC,  LT_SPC,  LT_TAB,  LT_ENT,  LT_BSPC, KC.DEL,
    ],                  
    # NAV
    [
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO,   KC.ESC,  KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        KC.NO,   KC.RALT, KC.NO,   KC.NO,   KC.NO,   KC.INS,  KC.HOME, KC.PGDN, KC.PGUP, KC.END,
                          KC.NO,   KC.NO,   KC.NO,   KC.ENT,  KC.BSPC, KC.NO,
    ],
    # FUN
    [
        KC.MUTE, KC.VOLD, KC.VOLU, KC.NO,   KC.NO,   KC.PSCR, KC.F1,   KC.F4,   KC.F7,   KC.F10,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.CAPS, KC.INS,  KC.F2,   KC.F5,   KC.F8,   KC.F11,
        KC.MPRV, KC.MSTP, KC.MPLY, KC.MNXT, KC.NO,   KC.NO,   KC.F3,   KC.F6,   KC.F9,   KC.F12,
                          KC.NO,   KC.NO,   KC.NO,   KC.DEL,  KC.ESC,  KC.NO,
    ],
    # SYM
    [
        KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.COLN, KC.DLR,  KC.PERC, KC.CIRC, KC.PLUS, KC.NO,   KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.PIPE, KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.NO,
                          KC.NO,   KC.RPRN, KC.UNDS, KC.NO,   KC.NO,   KC.NO,
    ],
    # NUM
    [
        KC.LBRC, KC.N7,   KC.N8,   KC.N9,   KC.RBRC, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.SCLN, KC.N4,   KC.N5,   KC.N6,   KC.EQL,  KC.NO,   KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.BSLS, KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.NO,
                          KC.NO,   KC.N0,   KC.MINS, KC.NO,   KC.NO,   KC.NO,
    ],

]

if __name__ == '__main__':
    keyboard.go()
