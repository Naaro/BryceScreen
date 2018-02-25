import RPi.GPIO as GPIO
import time
import socket

# GPIO Stuff
GPIO.setmode(GPIO.BOARD)
GreenLED=7
BlueLED=11
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.output(BlueLED,False)
GPIO.output(GreenLED,False)


# Network Stuff
s = socket.socket()
host = '192.168.0.17'
port = 9001
Enabled = True


#Begin
print ('Server Started!')
print ('Waiting for clients...')

s.bind((host,port))
s.listen(5)
c, addr = s.accept()
print ('Got Connection : ',addr)

def RunCommands(cmd):
    if msg == '<Exit>':
        print ('Shutting Down')
        Enabled = False
        c.close()
        GPIO.cleanup()
    elif msg == '<GreenOn>':
        GPIO.output(GreenLED,True)
    elif msg == '<GreenOff>':
        GPIO.output(GreenLED,False)
    elif msg == '<BlueOn>':
        GPIO.output(BlueLED,True)
    elif msg == '<BlueOff>':
        GPIO.output(BlueLED,False)
    else:
        print (addr, ' >>  ', msg)
    

try:
    while Enabled:
        msg = c.recv(256)
        RunCommands(msg)
        
        
except KeyboardInterrupt:
    pass
finally:
    c.close()
    GPIO.cleanup()
