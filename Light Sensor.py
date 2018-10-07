import RPi.GPIO as GPIO
import time



# 3v3=1
LightSensor=7
RedLED=11
GreenLED=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedLED,GPIO.OUT)
GPIO.setup(GreenLED,GPIO.OUT)

def rc_time (LightSensor):
    count=0

    GPIO.setup(LightSensor,GPIO.OUT)
    GPIO.output(LightSensor,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(LightSensor,GPIO.IN)
    while (GPIO.input(LightSensor) == GPIO.LOW):
        count+=1
        print('output : ' + str(count))
    return count


try:
    while True:
        Output=rc_time(LightSensor)
        #print(str(Output))
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
