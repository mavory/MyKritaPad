import usb_hid

# Umozni desce hlasit se pocitaci jako:
# 1. KLAAVESNICE (pro kc.F1-F9)
# 2. CONSUMER_CONTROL (pro mediální klávesy jako Volume Up/Down a Brightness)

usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.CONSUMER_CONTROL,
    )
)
