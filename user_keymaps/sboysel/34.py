from kb import KMKKeyboard, isRight
keyboard = KMKKeyboard()

from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())

# === layer tap ---------------------------------------------------------------
keyboard.tap_time = 200
# FUN (layer 1)
LT_SPC = KC.LT(1, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=keyboard.tap_time)
# NAV (layer 2)
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
    """
    0:BASE (QWERTY)

    /-----+-----+-----+-----+-----\         /-----+-----+-----+-----+-----\       
    |  q  |  w  |  e  |  r  |  t  |         |  y  |  u  |  i  |  o  |  p  |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  a  |  s  |  d  |  f  |  g  |         |  h  |  j  |  k  |  l  |  '  |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  z  |  x  |  c  |  v  |  b  |         |  n  |  m  |  ,  |  .  |  /  |
    \-----+-----+-----+-----+-----/         \-----+-----+-----+-----+-----/

                      /-----+-----\         /-----+-----\
                      | TAB | SPC |         | BSPC| ENT |
                      \-----+-----/         \-----+-----/
    Layers:
                       (FUN) (NAV)           (SYM) (NUM)
    """
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        MT_A,    MT_S,    MT_D,    MT_F,    KC.G,    KC.H,    MT_J,    MT_K,    MT_L,    MT_QUOT,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
        KC.NO,   KC.NO,   KC.NO,   LT_TAB,  LT_SPC,  LT_BSPC, LT_ENT,  KC.NO,   KC.NO,   KC.NO  
    ],                  
    """
    1:FUN

    /-----+-----+-----+-----+-----\         /-----+-----+-----+-----+-----\       
    | Mute| Vol-| Vol+|     |     |         |PrScr| F1  | F4  | F7  | F10 |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    | GUI | ALT | CTL | SFT |CpsLk|         | Ins | F2  | F5  | F8  | F11 |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    | Prev| Stop| Play| Next|     |         |     | F3  | F6  | F9  | F12 |
    \-----+-----+-----+-----+-----/         \-----+-----+-----+-----+-----/

                      /-----+-----\         /-----+-----\
                      | ~*~ |     |         | DEL | ESC |
                      \-----+-----/         \-----+-----/
    """
    [
        KC.MUTE, KC.VOLD, KC.VOLU, KC.NO,   KC.NO,   KC.PSCR, KC.F1,   KC.F4,   KC.F7,   KC.F10,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.CAPS, KC.INS,  KC.F2,   KC.F5,   KC.F8,   KC.F11,
        KC.MPRV, KC.MSTP, KC.MPLY, KC.MNXT, KC.NO,   KC.NO,   KC.F3,   KC.F6,   KC.F9,   KC.F12,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.DEL,  KC.ESC,  KC.NO,   KC.NO,   KC.NO
    ],
    """
    2:NAV


    /-----+-----+-----+-----+-----\         /-----+-----+-----+-----+-----\       
    |     |     |     |     |     |         |     |     |     |     |     |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    | GUI | ALT | CTL | SFT |     |         | ESC | LEFT| DOWN|  UP |RIGHT|
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |     |     |     |     |     |         | INS | HOME| PGDN| PGUP| END |
    \-----+-----+-----+-----+-----/         \-----+-----+-----+-----+-----/

                      /-----+-----\         /-----+-----\
                      |     | ~*~ |         | BSPC| ENT |
                      \-----+-----/         \-----+-----/
    """
    [
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO,   KC.ESC,  KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        KC.NO,   KC.RALT, KC.NO,   KC.NO,   KC.NO,   KC.INS,  KC.HOME, KC.PGDN, KC.PGUP, KC.END,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.BSPC, KC.ENT,  KC.NO,   KC.NO,   KC.NO
    ],
    """
    3:SYM

    /-----+-----+-----+-----+-----\         /-----+-----+-----+-----+-----\       
    |  {  |  &  |  *  |  (  |  }  |         |     |     |     |     |     |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  :  |  $  |  %  |  ^  |  +  |         |     | SFT | CTL | ALT | GUI | 
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  ~  |  !  |  @  |  #  |  |  |         |     |     |     |     |     |
    \-----+-----+-----+-----+-----/         \-----+-----+-----+-----+-----/

                      /-----+-----\         /-----+-----\
                      |  )  |  _  |         | ~*~ |     |
                      \-----+-----/         \-----+-----/
    """
    [
        KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.COLN, KC.DLR,  KC.PERC, KC.CIRC, KC.PLUS, KC.NO,   KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.PIPE, KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.RPRN, KC.UNDS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO
    ],
    """
    4:NUM

    /-----+-----+-----+-----+-----\         /-----+-----+-----+-----+-----\       
    |  [  |  7  |  8  |  9  |  ]  |         |     |     |     |     |     |
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  ;  |  4  |  5  |  6  |  =  |         |     | SFT | CTL | ALT | GUI | 
    |-----+-----+-----+-----+-----|         |-----+-----+-----+-----+-----|       
    |  `  |  1  |  2  |  3  |  \  |         |     |     |     |     |     |
    \-----+-----+-----+-----+-----/         \-----+-----+-----+-----+-----/

                      /-----+-----\         /-----+-----\
                      |     |  -  |         |     | ~*~ |
                      \-----+-----/         \-----+-----/
    """
    [
        KC.LBRC, KC.N7,   KC.N8,   KC.N9,   KC.RBRC, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.SCLN, KC.N4,   KC.N5,   KC.N6,   KC.EQL,  KC.NO,   KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.BSLS, KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.N0,   KC.MINS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO
    ],

]

if __name__ == '__main__':
    keyboard.go()
