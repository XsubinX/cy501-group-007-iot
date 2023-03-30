import RPi.GPIO as GPIO


DOOR_SENSOR_PIN = 40

def get_door_pin_status():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DOOR_SENSOR_PIN,GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return GPIO.input(DOOR_SENSOR_PIN)


#Test
status_code = get_door_pin_status()

if(status_code == 1):
   print('Door is open')
elif(status_code == 0):
   print('Door is closed')
else:
   print('Door sensor error')