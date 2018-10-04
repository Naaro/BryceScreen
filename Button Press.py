import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

Button=3
LED=5
BPress=False

GPIO.setup(Button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,False)


try: 
    while True:
        if GPIO.input(Button)==0 and BPress==False:
            print('Power : On')
            BPress=True
            GPIO.output(LED,True)
            time.sleep(0.3)
        elif GPIO.input(Button)==0 and BPress==True:
            print('Power : Off')
            BPress=False
            GPIO.output(LED,False)
            time.sleep(0.3)
        time.sleep(0.1)
        
finally:
    # Reset GIP Pins to a safe state
    GPIO.output(LED,False)
    GPIO.cleanup()
