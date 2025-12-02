# MyKritaPad

MyKritaPad is a custom 9-key macropad powered by a Seeed Studio XIAO RP2040!
It includes 9 mechanical switches wired through 9 diodes, 12 SK6812 MINI-E RGB LEDs for backlighting, and two EC11 rotary encoders for additional input control. ⭐

## Why did I do this?

I wanted to try something completely new that I had never done before. I was very interested in how everyone can create their own mini keyboard, so I tried it too.

## Notes

I started on Friday, October 28th. That day I saw that I could make my own mini keyboard, I registered and downloaded the programs. Then I opened KiCad and told myself that I would never do it (it was like flying a plane for the first time). Well, I had to overcome myself and started creating with it. At first it was terrible, but somehow I got over it.

Unfortunately, on October 29th I got sick and couldn't do anything at all, but on November 30th I overcame myself and started creating the first designs for my KritaPad. When I created it with it, I moved to Fusion, which I also looked into, what it was... Somehow I did it, even though I don't want to think about it.

Then on December 1st I overcame myself and spent the whole day at the computer to finish it. In the evening I finished and submitted the project.

## Features
- 9 mechanical keys  
- 9x diodes for proper key isolation  
- 10x SK6812 MINI-E addressable RGB LEDs  
- 2x EC11 rotary encoders
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

![image](https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-01%20135100.png?raw=true)

### PCB Layout
(I know, it's terrible.)

![image](https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-01%20133912.png?raw=true)

![image](https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-02%20151355.png?raw=true)

### Top view

![image](https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-01%20181425.png?raw=true)

![image](https://github.com/mavory/MyKritaPad/blob/main/Trash/Sn%C3%ADmek%20obrazovky%202025-12-01%20151754.png?raw=true)

## Firmware
The macropad can be programmed using KMK,... or any custom RP2040 firmware.  

## BOM

### Custom Components
- 1x Custom PCB  
- 1x 3D printed case (top, bottom - Black)
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

## Info
This macropad is made as part of the Hack Club Hackpad program! ✨


