import RPi.GPIO as GPIO
import time

Button=7
Buzzer=11
BPress=False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer,GPIO.OUT)


try: 
    while True:
        if GPIO.input(Button)==0 and BPress==False:
            print('Buzzer : On')
            BPress=True
            GPIO.output(Buzzer,True)
            time.sleep(0.3)
        elif GPIO.input(Button)==0 and BPress==True:
            print('Buzzer : Off')
            BPress=False
            GPIO.output(Buzzer,False)
            time.sleep(0.3)
        time.sleep(0.1)
        
finally:
    # Reset GIP Pins to a safe state
    GPIO.output(Buzzer,False)
    GPIO.cleanup()
