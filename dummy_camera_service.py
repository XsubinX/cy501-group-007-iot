from time import sleep

def capture_image():
    print('Inside capture_image')
    sleep(2)
    file_name='static/camera/latest.jpeg'
    return file_name