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
host = '192.168.0.20'
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
    if cmd == '<Exit>':
        print ('Shutting Down')
        Enabled = False
        c.close()
        GPIO.cleanup()
    elif cmd == '<GreenOn>':
        print('Green On')
        GPIO.output(GreenLED,True)
    elif cmd == '<GreenOff>':
        print('Green Off')
        GPIO.output(GreenLED,False)
    elif cmd == '<BlueOn>':
        print('Blue On')
        GPIO.output(BlueLED,True)
    elif cmd == '<BlueOff>':
        print('Blue Off')
        GPIO.output(BlueLED,False)
    elif cmd == 'send':
        c.send(b'this is a test')
    else:
        print (addr, ' >>  ', cmd)
    

try:
    while Enabled:
        msg = c.recv(512)
        RunCommands(str(msg.decode()))
except KeyboardInterrupt:
    pass
finally:
    c.close()
    GPIO.cleanup()
