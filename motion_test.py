import RPi.GPIO as GPIO
from time import sleep

PIR_input = 29
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_input, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    curr_status=GPIO.input(PIR_input)
    print(curr_status)
    if(curr_status):
        print("motion detected")
        sleep(2)
    else:
        print("no motion")
        sleep(2)