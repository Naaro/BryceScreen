import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# 3v3=1
LightSensor=7
RedLED=11
GreenLED=13

def rc_time (LightSensor):
    count=0

    GPIO.setup(LightSensor,GPIO.OUT)
    GPIO.output(LightSensor,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(LightSensor,GPIO.IN)
    while (GPIO.input(LightSensor) == GPIO.LOW):
        count+=1
    return count

try:
    GPIO.setup(RedLED,GPIO.OUT)
    GPIO.setup(GreenLED,GPIO.OUT)
    while True:
        Output=rc_time(LightSensor)
        print Output
        if Output>5000:
            GPIO.output(RedLED,True)
            GPIO.output(GreenLED,False)
        else:
            GPIO.output(RedLED,False)
            GPIO.output(GreenLED,True)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
