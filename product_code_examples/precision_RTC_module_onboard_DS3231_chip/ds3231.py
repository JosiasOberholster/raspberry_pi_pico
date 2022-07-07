#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Class to set time (YYYY/MM/DD HH:MM:SS DAY_OF_THE_WEEK),
this class also allows for a alarm to be set.

NB: When setting the date for the first time, use
the function set_time('HH:MM:SS,DAY_OF_THE_WEEK,YYYY-MM-DD').
This function is inded to be used only once to set the time
and date, other than that it should not be used again, as it
will constantly reset the time to the supplied time date.
"""
from machine import Pin, I2C
import time
import binascii

"""
Variables
"""
ALARM_PIN = 3

class ds3231(object):
    # The register value is the binary-coded decimal (BCD) format:
    # sec min hour week day month year
    NowTime = b'\x00\x45\x13\x02\x24\x05\x21'
    w  = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    address = 0x68
    start_reg = 0x00
    alarm1_reg = 0x07
    control_reg = 0x0e
    status_reg = 0x0f
    
    """
    Init function
    
    @returns void
    """
    def __init__(self):
        # The first version use i2c1
        #I2C_PORT = 1
        #I2C_SDA = 6
        #I2C_SCL = 7
        # The new version use i2c0,if it dont work,try to uncomment the line 14 and
        # comment line 17.
        # It should solder the R3 with 0R resistor if want to use alarm function,please
        # refer to the Sch file on waveshare Pico-RTC-DS3231 wiki
        # https://www.waveshare.net/w/upload/0/08/Pico-RTC-DS3231_Sch.pdf
        I2C_PORT = 0
        I2C_SDA = 20
        I2C_SCL = 21
        self.bus = I2C(I2C_PORT,scl=Pin(I2C_SCL),sda=Pin(I2C_SDA))

    """
    Set the current time and date
    
    @param string new_time Set the current time and date by the format:
                           'HH:MM:SS,DAY_OF_THE_WEEK,YYYY-MM-DD'. Time
                           is set in 24Hours.
    
    @returns void
    """
    def set_time(self,new_time):
        hour = new_time[0] + new_time[1]
        minute = new_time[3] + new_time[4]
        second = new_time[6] + new_time[7]
        week = "0" + str(self.w.index(new_time.split(",",2)[1])+1)
        year = new_time.split(",",2)[2][2] + new_time.split(",",2)[2][3]
        month = new_time.split(",",2)[2][5] + new_time.split(",",2)[2][6]
        day = new_time.split(",",2)[2][8] + new_time.split(",",2)[2][9]
        now_time = binascii.unhexlify((second + " " + minute + " " + hour + " " + week + " " + day + " " + month + " " + year).replace(' ',''))
        self.bus.writeto_mem(int(self.address),int(self.start_reg),now_time)
    
    """
    Read the current date and time. The date and time must be set at least
    once before running this value.
    
    @returns string
    """
    def read_time(self):
        t = self.bus.readfrom_mem(int(self.address),int(self.start_reg),7)
        a = t[0]&0x7F  #second
        b = t[1]&0x7F  #minute
        c = t[2]&0x3F  #hour
        d = t[3]&0x07  #week
        e = t[4]&0x3F  #day
        f = t[5]&0x1F  #month
        return "20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],self.w[t[3]-1])
    
    def get_time(self):
        ct = self.read_time()
        curr_time = ct[11]+ct[12]+ct[13]+ct[14]+ct[15]+ct[16]+ct[17]+ct[18]
        return curr_time;

    """
    Set a alarm.
    
    @params string Date time to set the alarm. The value should be in
                   the following format: 'HH:MM:SS,DAY_OF_THE_WEEK,YYYY-MM-DD'.
                   Time is set in 24Hours.
    
    @returns 
    """
    def set_alarm_time(self,alarm_time):
        # init the alarm pin
        self.alarm_pin = Pin(ALARM_PIN,Pin.IN,Pin.PULL_UP)
        # set alarm irq
        self.alarm_pin.irq(lambda pin: print("alarm1 time is up"), Pin.IRQ_FALLING)
        # enable the alarm1 reg
        self.bus.writeto_mem(int(self.address),int(self.control_reg),b'\x05')
        # convert to the BCD format
        hour = alarm_time[0] + alarm_time[1]
        minute = alarm_time[3] + alarm_time[4]
        second = alarm_time[6] + alarm_time[7]
        date = alarm_time.split(",",2)[2][8] + alarm_time.split(",",2)[2][9]
        now_time = binascii.unhexlify((second + " " + minute + " " + hour +  " " + date).replace(' ',''))
        # write alarm time to alarm1 reg
        self.bus.writeto_mem(int(self.address),int(self.alarm1_reg),now_time)
        