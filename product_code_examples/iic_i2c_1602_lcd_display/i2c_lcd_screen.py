import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
sdaPin = machine.Pin(0)
sclPin = machine.Pin(1)

i2c = I2C(0, sda=sdaPin, scl=sclPin, freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

#while True:
#    lcd.putstr("Lets Count 0-10!")
#    sleep(2)
#    lcd.clear()
#    for i in range(10):
#       lcd.putstr(str(i))
#        sleep(1)
#        lcd.clear()

while True:
    lcd.putstr("Hello IT.")
    sleep(3)
    lcd.clear()
    lcd.putstr("Have you tried  switching it")
    sleep(3)
    lcd.clear()
    lcd.putstr("off and on again?")
    sleep(3)
    lcd.clear()