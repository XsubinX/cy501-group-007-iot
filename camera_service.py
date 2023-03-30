from picamera import PiCamera
from time import sleep

def capture_image():
    camera = PiCamera()
    # Initialize camera
    sleep(2)
    file_name='/home/subin/group007/iot/cy501-group-007-iot/files/camera/latest.jpg'
    camera.capture(file_name)
    return file_name


# Test
print('Image ready %s'% capture_image())