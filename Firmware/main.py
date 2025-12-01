'''
Kód pro 3x3 macropad s 2x EC11 encodery a 12x SK6812 MINI-E RGB LED.
Klávesy mapovány na F1-F9. Obsahuje efekt RGB Fade In při startu.
'''

import board
import neopixel
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner, DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import Encoder
from kmk.modules.rgb import RGB, RGBModes
from kmk.modules.layers import Layers

# ----------------------------------------------------
# 1. NASTAVENÍ HARDWARU
# ----------------------------------------------------

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# --- Matice 3 Řádky x 3 Sloupce (9 kláves) ---
ROW_PINS = [
    board.GP26, # RA1
    board.GP27, # RA2
    board.GP28  # RA3
]
COL_PINS = [
    board.GP3,  # SL1
    board.GP4,  # SL2
    board.GP29  # SL3 (volný pin pro 3. sloupec)
]

DIODE_ORIENTATION = DiodeOrientation.COL2ROW 

keyboard.matrix = MatrixScanner(
    cols=COL_PINS,
    rows=ROW_PINS,
    diode_orientation=DIODE_ORIENTATION
)

# --- Encodery (2x EC11) ---
encoder_handler = Encoder()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    # Encoder 1: Pin A/B (GP6, GP7)
    (board.GP6, board.GP7, KC.TRNS),
    # Encoder 2: Pin A/B (GP2, GP1)
    (board.GP2, board.GP1, KC.TRNS),
)

# --- RGB LED (12x SK6812) ---
NUM_PIXELS = 12 # **Změněno na 12**
PIXEL_PIN = board.GP0 # Pin pro data LED

# Inicializace RGB (KMK modul)
rgb = RGB(
    pixel_pin=PIXEL_PIN,
    num_pixels=NUM_PIXELS, # **Změněno na 12**
    val_limit=255, 
    rgb_mode=RGBModes.STATIC,
    on_init=False, 
)
keyboard.modules.append(rgb)

# ----------------------------------------------------
# 2. MAPA KLÁVES A ENCODERŮ
# ----------------------------------------------------

# Klávesy F1 až F9 v matici 3x3
keyboard.keymap = [
    # BASE LAYER (Vrstva 0)
    [
        # SL1   SL2   SL3
        KC.F7, KC.F8, KC.F9,   # RA1
        KC.F4, KC.F5, KC.F6,   # RA2
        KC.F1, KC.F2, KC.F3    # RA3
    ]
]

# Encoder Mapování
encoder_handler.map = (
    # Vrstva 0 (BASE)
    (
        # Encoder 1 (index 0) - Hlasitost
        (KC.VOLU, KC.VOLD, KC.TRNS),
        # Encoder 2 (index 1) - Jas obrazovky (Brightness)
        (KC.BRMU, KC.BRMD, KC.TRNS), 
    ),
)


# ----------------------------------------------------
# 3. START KMK A FADE IN EFEKT
# ----------------------------------------------------

if __name__ == '__main__':
    pixels = rgb.pixels 

    # --- Implementace FADE IN efektu ---
    TARGET_COLOR = (150, 0, 150) # Tmavší fialová
    FADE_STEPS = 50
    FADE_DELAY = 0.01 

    for step in range(FADE_STEPS):
        ratio = step / FADE_STEPS
        
        r = int(TARGET_COLOR[0] * ratio)
        g = int(TARGET_COLOR[1] * ratio)
        b = int(TARGET_COLOR[2] * ratio)
        
        # Nastavíme barvu na všech 12 pixelech
        pixels.fill((r, g, b))
        pixels.show()
        time.sleep(FADE_DELAY)

    # Po dokončení fade in předáme řízení KMK
    keyboard.go()
