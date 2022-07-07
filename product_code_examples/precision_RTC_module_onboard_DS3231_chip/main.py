from ds3231 import ds3231

rtc = ds3231()
#rtc.set_time('17:12:10,Tuesday,2022-07-05')
#rtc.set_alarm_time('13:45:55,Monday,2021-05-24')
while True:      
    currentTime = rtc.read_time()
    print(currentTime)
    time.sleep(1)