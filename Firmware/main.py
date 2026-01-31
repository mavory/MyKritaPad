import board
import neopixel
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(EncoderHandler())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())

# mega tvrdy reset!
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True)

def force_reset_led(color):
    # 1. resetik
    pixel[0] = (0, 0, 0)
    time.sleep(0.01) # pauza, ale jako fakt krátká
    # 2. nova barva
    pixel[0] = color
    pixel.show()

force_reset_led((0, 0, 255)) # blueeee

# tlačitka pro reset,...
class LayerResetKey:
    def __init__(self, layer, color):
        self.layer = layer
        self.color = color

    def on_press(self, keyboard, coord_int=None):
        force_reset_led(self.color)
        return KC.TO(self.layer).on_press(keyboard, coord_int)

    def on_release(self, keyboard, coord_int=None):
        return KC.TO(self.layer).on_release(keyboard, coord_int)

# definice resetovacích věci
GO_L0 = LayerResetKey(0, (0, 0, 255))
GO_L1 = LayerResetKey(1, (255, 0, 0))
GO_L2 = LayerResetKey(2, (0, 255, 0))

# matice
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D9, board.D10, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

encoder_handler = keyboard.modules[1]
encoder_handler.pins = ((board.D4, board.D5, None, True), (board.D8, board.D7, None, True))
encoder_handler.divisor = 4
encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN), (KC.LCTL(KC.TAB), KC.LCTL(KC.LSFT(KC.TAB)))),
    ((KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK), (KC.MWEL_UP, KC.MWEL_DOWN)),
    ((KC.LCTL(KC.PENT), KC.LCTL(KC.PMNS)), (KC.PGUP, KC.PGDN)),
]

# mapování vrstev přes SW9
keyboard.keymap = [
    [   # modricka barvicka L0
        KC.F14,         KC.F15,         KC.F16,
        KC.LALT(KC.F4), KC.LGUI(KC.L),  KC.LGUI(KC.LSFT(KC.S)),
        KC.LCTL(KC.C),  KC.LCTL(KC.V),  KC.TD(KC.AUDIO_MUTE, GO_L1) 
    ],
    [   # cervena barva L1
        KC.MEDIA_PLAY_PAUSE, KC.CALCULATOR,  KC.LCTL(KC.LSFT(KC.ESC)),
        KC.LGUI(KC.LEFT),    KC.LGUI(KC.UP),  KC.LGUI(KC.RIGHT),
        KC.LCTL(KC.A),       KC.LCTL(KC.X),  KC.TD(KC.AUDIO_MUTE, GO_L2) 
    ],
    [   # zelena barva L2
        KC.F5,               KC.F10,          KC.F11,
        KC.LCTL(KC.F),       KC.LCTL(KC.B),   KC.LCTL(KC.P),
        KC.LCTL(KC.LSFT(KC.K)), KC.LCTL(KC.LSFT(KC.P)), KC.TD(KC.AUDIO_MUTE, GO_L0) 
    ]
]

if __name__ == '__main__':
    keyboard.go()
