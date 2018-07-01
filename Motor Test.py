import RPi.GPIO as GPIO
import time
import socket

# GPIO Stuff
GPIO.setmode(GPIO.BOARD)
Motor1Forward=7
Motor1Backward=11
Motor2Forward=13
Motor2Backward=12
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(Motor1Forward,False)
GPIO.output(Motor1Backward,False)
GPIO.output(Motor2Forward,False)
GPIO.output(Motor2Backward,False)


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
    #print (addr, ' >>  ', msg)
    if msg == '<Exit>':
        print ('Shutting Down')
        GPIO.output(Motor1Forward,False)
        GPIO.output(Motor1Backward,False)
        GPIO.output(Motor2Forward,False)
        GPIO.output(Motor2Backward,False)
        Enabled = False
        c.close()
        GPIO.cleanup()
    elif msg == '<Forward>':
        GPIO.output(Motor1Backward,False)
        GPIO.output(Motor2Backward,False)
        GPIO.output(Motor1Forward,True)
        GPIO.output(Motor2Forward,True)
    elif msg == '<Backward>':
        GPIO.output(Motor1Forward,False)
        GPIO.output(Motor2Forward,False)
        GPIO.output(Motor1Backward,True)
        GPIO.output(Motor2Backward,True)
    elif msg == '<Left>':
	GPIO.output(Motor1Forward,False)
	GPIO.output(Motor1Backward,False)
	GPIO.output(Motor2Backward,False)
	GPIO.output(Motor2Forward,True)
    elif msg == '<Right>':
	GPIO.output(Motor2Forward,False)
	GPIO.output(Motor2Backward,False)
	GPIO.output(Motor1Backward,False)
	GPIO.output(Motor1Forward,True)
    elif msg == '<Idle>':
        GPIO.output(Motor1Forward,False)
        GPIO.output(Motor1Backward,False)
        GPIO.output(Motor2Forward,False)
        GPIO.output(Motor2Backward,False)
    else:
        print (addr, ' >>  ', msg)
    

try:
    while Enabled:
        msg = c.recv(128)
        RunCommands(msg)
except KeyboardInterrupt:
    pass
finally:
    c.close()
    GPIO.cleanup()
