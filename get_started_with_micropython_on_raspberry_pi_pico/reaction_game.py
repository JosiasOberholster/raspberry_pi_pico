import machine
import utime
import urandom

pressed = False
fastest_button = None
led = machine.Pin(15, machine.Pin.OUT)
player_one_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
player_two_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
player_three_button = machine.Pin(17, machine.Pin.IN , machine.Pin.PULL_DOWN)


def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        global fastest_button
        fastest_button = pin
        
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

player_one_button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
player_two_button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
player_three_button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
timer_start = utime.ticks_ms()

while fastest_button is None:
    utime.sleep(1)
    
if fastest_button is player_one_button:
    print('player one won')
elif fastest_button is player_two_button:
    print('player two won')
elif fastest_button is player_three_button:
    print('player three won')
