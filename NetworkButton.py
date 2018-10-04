import RPi.GPIO as GPIO
import time
import socket

# GPIO Stuff
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
Button=3
LED=5
GPIO.setup(Button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,False)


# Network Stuff
s = socket.socket()
host = '192.168.0.24'
port = 9001
Enabled = True


#Begin
print ('Listener Started!')
print ('Waiting for Connection to Command...')

s.bind((host,port))
s.listen(5)
c, addr = s.accept()
print ('Connection Established : ',addr)
print(' ')


BPress = False
try: 
    while True:
        if GPIO.input(Button)==0 and BPress==False:
            print('Power : On')
            c.send(b'LED Power On')
            BPress=True
            time.sleep(0.3)
        elif GPIO.input(Button)==0 and BPress==True:
            print('Power : Off')
            c.send(b'LED Power On')
            BPress=False
            GPIO.output(LED,False)
            time.sleep(0.3)
        time.sleep(0.1)
finally:
    # Reset GIP Pins to a safe state
    c.close()
    GPIO.output(LED,False)
    GPIO.cleanup()
