from picamera import PiCamera
from time import sleep
import random

def capture_image():
    camera = PiCamera()
    # Initialize camera
    sleep(2)
    file_name='/home/subin/group007/iot/cy501-group-007-iot/static/camera/latest.jpeg'
    camera.capture(file_name)
    camera.close()
    random_number=random.randint(0,9)
    return f"/static/camera/latest.jpeg?refresh={random_number}"


# Test
print('Image ready %s'% capture_image())