import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

rgb = RGB(
    pixel_pin=board.NEOPIXEL, 
    num_pixels=1, 
    val_default=50, 
    animation_mode=AnimationModes.RAINBOW,
    animation_speed=2
)
keyboard.extensions.append(rgb)

# enkondery
encoder_handler.pins = (
    (board.D4, board.D5, None, True), 
    (board.D8, board.D7, None, True), 
)
encoder_handler.map = [
    (
        (KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN), 
        (KC.LCTL(KC.TAB), KC.LCTL(KC.LSFT(KC.TAB)))
    ),
]

# matkaaa
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D9, board.D10, board.D3) 
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# mapa tlačítek
keyboard.keymap = [
    [
        # 1. ŘADA: Chrome, Slack, Spotify
        KC.F14,            KC.F15,            KC.F16, 
        
        # 2. ŘADA: Systém
        KC.LALT(KC.F4),    KC.LGUI(KC.L),     KC.LGUI(KC.LSFT(KC.S)),
        
        # 3. ŘADA: Nástroje
        KC.LCTL(KC.C),     KC.LCTL(KC.V),     KC.AUDIO_MUTE           
    ]
]

if __name__ == '__main__':
    keyboard.go()
