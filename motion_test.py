import RPi.GPIO as GPIO

PIR_input = 29				#read PIR Output
LED = 32				#LED for signalling motion detected	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
    if(GPIO.input(PIR_input)):
        print(1) # motion detected
    else:
        print(0) # no motion