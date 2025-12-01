# MyKritaPad

MyKritaPad is a custom 9-key macropad powered by a Seeed Studio XIAO RP2040!
It includes 9 mechanical switches wired through 9 diodes, 12 SK6812 MINI-E RGB LEDs for backlighting, and two EC11 rotary encoders for additional input control.

## Features
- 9 mechanical keys  
- 9x diodes for proper key isolation  
- 10x SK6812 MINI-E addressable RGB LEDs  
- 2x EC11 rotary encoders (A/B + switch)  
- Powered by Seeed Studio XIAO RP2040  
- Designed for use with KMK or custom firmware  

## PCB
The PCB is designed in KiCad and includes:
- 9 key switch footprints  
- diode matrix wiring  
- daisy-chained SK6812 MINI-E LEDs  
- pins for two rotary encoders  
- XIAO RP2040 as the main controller  

### Schematic
*(Insert schematic image here)*

### PCB Layout
(https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-01%20133912.png?raw=true)

## Firmware
The macropad can be programmed using KMK,... or any custom RP2040 firmware.  

## BOM

### Custom Components
- 1x Custom PCB  
- 1x 3D printed case (top, bottom)
- 9x keycaps  

### COTS Components
- 9x mechanical switches (MX style)  
- 9x Blank DSA keycaps
- 9x 1N4148 diodes  
- 12x SK6812 MINI-E LEDs  
- 2x EC11 rotary encoders  
- 1x Seeed Studio XIAO RP2040    
- 4x M3 x 6mm Screws
- 4x M3x5mx4mm heatset inserts

## Notes
This macropad is made as part of the Hack Club Hackpad program! ✨
