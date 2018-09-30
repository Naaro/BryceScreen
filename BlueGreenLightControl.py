import RPi.GPIO as GPIO
import time
import os

# GPIO Stuff
GPIO.setwarnings(False) # Disable Warnings
GPIO.setmode(GPIO.BOARD) # Set the GPIO mode type (for pin  indication it's either GPIO#, or Board Pin #)
GreenLED = 11 # GreenLED is Pin # 11 on the board
BlueLED = 13 # BlueLED is Pin # 13 on the board
GPIO.setup(GreenLED,GPIO.OUT) # Set the output mode for the GreenLED pin 
GPIO.setup(BlueLED,GPIO.OUT) # Set the output mode for the BlueLED pin 
GPIO.output(GreenLED,False) 
GPIO.output(BlueLED,False)


Running = True

# Prints out the available Commands
def PrintCommands():
	print('=== Available Commands ===')
	print('Quit : Ends the script')
	print('Green On : Turns on the Green LED')
	print('Green Off : Turns on the Green LED')
	print('Blue On : Turns on the Blue LED')
	print('Blue Off : Turns on the Blue LED')
	
# Turns the Blue LED on/off
def Blue(Value):
	GPIO.output(BlueLED,Value)
	
# Turns the Green LED on/off
def Green(Value):
	GPIO.output(GreenLED,Value) 

	
# Looping Script
while Running:
	Command = str(input('Command:'))
	if (Command == 'End'):
		Running = False
	elif (Command == 'Green On'):
		Green(True)
	elif (Command == 'Green Off'):
		Green(False)
	elif (Command == 'Blue On'):
		Blue(True)
	elif (Command == 'Blue Off'):
		Blue(False)
	elif (Command == '/?' or Command == '--?' or Command == '?' or Command == 'help'):
		PrintCommands()

GPIO.cleanup()		
