------------------------------------------
This is to explain how to connect sensor 
------------------------------------------

GND  -> GND
GP28 -> High/Low Output
VBUS -> +Power

------------------------------------------
Using the code:
------------------------------------------

There is nothing special about the code, 
this will only allow the sensor to work 
and detect as expected. Do keep in mind 
that there are two triggers that needs
manual adjustment to change how they work:
 - Single trigger mode
  - Time delay is started immediatey upon
    detecting motion. Continued detection
    is blocked.
 - Repeatable trigger mode 
  - Time delay is re-started every time 
    moton is detected.
