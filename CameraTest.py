from picamera import PiCamera
from time import sleep
from gpiozero import Button #gpio 17 used

button = Button(17)
camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/projects/TestImages/frame%03d.png' % frame)
        frame += 1
    except KeyboardIntertupt:
        camera.stop_preview()
        break

