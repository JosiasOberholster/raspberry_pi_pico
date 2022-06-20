import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_external_red = machine.Pin(13, machine.Pin.OUT)
led_external_blue = machine.Pin(14, machine.Pin.OUT)
led_external_yellow = machine.Pin(15, machine.Pin.OUT)
sleep_time = 0.4

led_onboard.value(0)         #off
led_external_red.value(0)    #off
led_external_blue.value(0)   #off
led_external_yellow.value(0) #off

led_onboard.toggle()  #on
while True:
    led_onboard.toggle()         #off
    led_external_red.toggle()    #on
    utime.sleep(sleep_time)
    led_external_red.toggle()    #off
    led_external_blue.toggle()   #on
    utime.sleep(sleep_time)
    led_external_blue.toggle()   #off
    led_external_yellow.toggle() #on
    utime.sleep(sleep_time)
    led_external_yellow.toggle() #off
    led_onboard.toggle()         #on
    utime.sleep(sleep_time)
    