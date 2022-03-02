import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)
button_value = 0

while True:
    if button.value() == 1:
        button_value = 1
    while button.value() == 1:
        led_external.value(1)
        if button_value == 1:
            button_value = 0
            print('led on')
    led_external.value(0)
