------------------------------------------
This is to explain how to connect the LCD 
display to the RP Pico:
------------------------------------------

GP0  -> SDA
GP1  -> SCL
VBUS -> VCC
GND  -> GND

------------------------------------------
Using the code:
------------------------------------------

Two main files are requried for 
functionality: 
  - lcd_api.py
  - pico_i2c_lcd.py
These two files were sourced and not 
written by me.

i2c_lcd_screen_device_address.py to get the 
device address, this s very important to run.

i2c_lcd_screen.py to run the function, if 
this file is used on the Raspberry Pi Pico, 
then it needs to be renamed to index.py. This
file is the main source to run the functions.