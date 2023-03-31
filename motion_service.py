import RPi.GPIO as GPIO
from time import sleep

MOTION_SENSOR_PIN = 19

def get_motion_sensor_pin_status():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MOTION_SENSOR_PIN,GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return GPIO.input(MOTION_SENSOR_PIN)


#Test
while True:
   status_code = get_motion_sensor_pin_status()
   print(status_code)
   sleep(5)
   #if status_code == 0:
      #print("movement detected")
      # sleep(5)
  # else:
      # print("Waiting for movement")
       #sleep(0.2)