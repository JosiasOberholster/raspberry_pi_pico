import machine
import utime

potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    led.duty_u16(potentiometer.read_u16())