import board

from kb import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())

# === layer tap ---------------------------------------------------------------
keyboard.tap_time = 200
# NAV (layer 1)
LT_TAB = KC.LT(1, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
LT_SPC = KC.LT(1, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# NUM (layer 2)
LT_ENT = KC.LT(2, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# SYM (layer 3)
LT_BSPC = KC.LT(3, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# FUN (layer 4)
LT_DEL = KC.LT(4, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# MEDIA (layer 5)
LT_ESC = KC.LT(5, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)

# === home row mods ------------------------------------------------------------
MT_A = KC.MT(KC.A, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_S = KC.MT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_D = KC.MT(KC.D, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)

MT_J = KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_K = KC.MT(KC.K, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_L = KC.MT(KC.L, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)
MT_QUOT = KC.MT(KC.QUOT, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=keyboard.tap_time)

# === keymap -------------------------------------------------------------------
keyboard.keymap = [
    # QWERTY
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,       KC.Y,   KC.U,    KC.I,    KC.O,    KC.P,
        MT_A,    MT_S,    MT_D,    MT_F,    KC.G,       KC.H,   MT_J,    MT_K,    MT_L,    MT_QUOT,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,       KC.N,   KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
        KC.NO,   KC.NO,   LT_ESC,  LT_SPC,  LT_TAB,     LT_ENT, LT_BSPC, LT_DEL,  KC.NO,   KC.NO
    ],                  
    #                     MEDIA             NAV         NUM     SYM      FUN
    # NAV
    [
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LALT, KC.LCTL, KC.LGUI, KC.LSFT, KC.NO,      KC.NO,  KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        KC.NO,   KC.RALT, KC.NO,   KC.NO,   KC.NO,      KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.ENT, KC.BSPC, KC.DEL,  KC.NO,   KC.NO
    ],
    # NUM
    [
        KC.LBRC, KC.N7,   KC.N8,   KC.N9,   KC.RBRC,    KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.SCLN, KC.N4,   KC.N5,   KC.N6,   KC.EQL,     KC.NO,  KC.LSFT, KC.LGUI, KC.LCTL, KC.LALT,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.BSLS,    KC.NO,  KC.NO,   KC.NO,   KC.RALT, KC.NO,
        KC.NO,   KC.NO,   KC.DOT,  KC.N0,   KC.MINS,    KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO
    ],
    # SYM
    [
        KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR,    KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.COLN, KC.DLR,  KC.PERC, KC.CIRC, KC.PLUS,    KC.NO,  KC.LSFT, KC.LGUI, KC.LCTL, KC.LALT,
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.PIPE,    KC.NO,  KC.NO,   KC.NO,   KC.RALT, KC.NO,
        KC.NO,   KC.NO,   KC.LPRN, KC.RPRN, KC.UNDS,    KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO
    ],
    # FUN
    [
        KC.F12,  KC.F7,   KC.F8,   KC.F9,   KC.PSCR,    KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.F11,  KC.F4,   KC.F5,   KC.F6,   KC.SLCK,    KC.NO,  KC.LSFT, KC.LGUI, KC.LCTL, KC.LALT,
        KC.F10,  KC.F1,   KC.F2,   KC.F3,   KC.PAUS,    KC.NO,  KC.NO,   KC.NO,   KC.RALT, KC.NO,
        KC.NO,   KC.NO,   KC.APP,  KC.SPC,  KC.TAB,     KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO
    ],
    # MEDIA
    [
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LALT, KC.LCTL, KC.LGUI, KC.LSFT, KC.NO,      KC.PS_TOG, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT,
        KC.NO,   KC.RALT, KC.NO,   KC.NO,   KC.NO,      KC.HID,    KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.MSTP,   KC.MPLY, KC.MUTE, KC.NO,   KC.NO
    ],
]

layer_names_list = [
    'QWERTY', 'NAV', 'NUM', 'SYM', 'FUN', 'MEDIA',
]

if __name__ == '__main__':
    print('board:   CrowBoard')
    print('keymap:  Miryoku KMK')
    keyboard.go()
