import RPi.GPIO as GPIO
import time
import socket

# GPIO Stuff
GPIO.setmode(GPIO.BOARD)
GreenLED=11
BlueLED=13
GPIO.setup(GreenLED,GPIO.OUT)
GPIO.setup(BlueLED,GPIO.OUT)
GPIO.output(BlueLED,False)
GPIO.output(GreenLED,False)


# Network Stuff
s = socket.socket()
host = '192.168.0.100'
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

def RunCommands(cmd):
    if msg == '<Exit>':
        print ('Shutting Down')
        Enabled = False
        c.close()
        GPIO.cleanup()
    elif msg == '<GreenOn>':
        print('Green On')
        GPIO.output(GreenLED,True)
    elif msg == '<GreenOff>':
        print('Green Off')
        GPIO.output(GreenLED,False)
    elif msg == '<BlueOn>':
        print('Blue On')
        GPIO.output(BlueLED,True)
    elif msg == '<BlueOff>':
        print('Blue Off')
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
