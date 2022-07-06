from lps22hbtr import LPS22HB
from icm20948 import ICM20948
import time

"""
Get temperature, pressure and dispalay it in the CLI
"""
lps22hb=LPS22HB()
icm20948=ICM20948()
while True:
    ##Get Temp and Pressure
#    TEMP_DATA = lps22hb._get_temp()
#    PRESS_DATA = lps22hb._get_pressure()
#    print('Pressure = ', PRESS_DATA , ' hPa\r')            
#    print('Temperature = ', str(TEMP_DATA), ' °C\r\n')
#    time.sleep(1)

    ##Get gyro, acceleration, magnetic, ptch, roll and yaw
    gyro = icm20948._get_Gyro()
    time.sleep(0.1)
    print('\r\nGyroscope:     X = %d , Y = %d , Z = %d\r\n'%(gyro[0],gyro[1],gyro[2]))

    accel = icm20948._get_Acceleration()
    time.sleep(0.1)
    print('\r\nAcceleration:  X = %d , Y = %d , Z = %d\r\n'%(accel[0],accel[1],accel[2])) 

    mag = icm20948._get_Magnetic()
    time.sleep(0.1)
    print('\r\nMagnetic:      X = %d , Y = %d , Z = %d\r\n'%((mag[0]),mag[1],mag[2]))

    pitchRollYaw = icm20948._get_pitch_roll_yaw()
    time.sleep(0.1)
    print('\r\nRoll = %.2f , Pitch = %.2f , Yaw = %.2f\r\n'%(pitchRollYaw[0],pitchRollYaw[1],pitchRollYaw[2]))