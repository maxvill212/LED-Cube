import RPi.GPIO as GPIO
from time import sleep

#Using BCM standard
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Initializing as output
#Order on LED left to right, front (close to breadboard) to back
#Cathode leads
GPIO.setup([14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22], GPIO.OUT, initial=GPIO.HIGH)
#Anode Leads, top to bottom)
GPIO.setup([5, 6, 13, 19], GPIO.OUT, initial=GPIO.LOW)

#Declaring columns and rows
column = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22]
row = [5, 6, 13, 19]


for i in range (5):
    for j in range(16):
        GPIO.output(column[j],0)
        sleep(0.5)
        GPIO.output(row[0],1)
print("done")
GPIO.cleanup()