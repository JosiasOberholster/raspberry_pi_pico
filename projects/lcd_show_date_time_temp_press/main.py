import machine
import time
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from ds3231 import ds3231
from lps22hbtr import LPS22HB

sdaPin = machine.Pin(16)
sclPin = machine.Pin(17)
i2c = I2C(0, sda=sdaPin, scl=sclPin, freq=400000)
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
rtc = ds3231()
lps22hb=LPS22HB()
#rtc.set_time('17:12:10,Tuesday,2022-07-05')
#rtc.set_alarm_time('13:45:55,Monday,2021-05-24')
while True:      
    ct = rtc.read_time()
    CURR_TEMP = lps22hb._get_temp()  
    CURR_TIME = rtc.get_time()
    CURR_DATE = rtc.get_date()
    CURR_WEEK = rtc.get_date_of_week()
    print(CURR_TIME)
    print(CURR_DATE)
    print(CURR_WEEK)
    print('Temp: ', str(CURR_TEMP), '°C')
    time.sleep(1)
    lcd.putstr("Hello IT.")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("Have you tried  switching it")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("off and on again?")
    time.sleep(3)
    lcd.clear()