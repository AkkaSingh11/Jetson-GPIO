import cv2
import RPi.GPIO as GPIO
import time

# Pin Definitions
input_pin = 18  # BCM pin 18, BOARD pin 12


cap = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)
count=0
def read_image():
	while cap.isOpened():
	    ret,frame = cap.read()
	    if not ret: break
	    print("count, shape = ", count, frame.shape)
	    cv2.imwrite(str(count) + ".png", frame)
	    count =count + 1
	    
	cap.release()

def main():
    prev_value = None
    show_camera()
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            value = GPIO.input(input_pin)
            if value != prev_value:
                if value == GPIO.HIGH:
                    value_str = "HIGH"
                else:
                    value_str = "LOW"
                print("Value read from pin {} : {}".format(input_pin,
                                                           value_str))
                prev_value = value
		read_image()
            time.sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
