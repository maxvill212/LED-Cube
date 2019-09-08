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

#Outer shell, then core
for i in range(3):
    #Outer shell
    for j in range(4):
        GPIO.output(column[j], 0)
    for j in range (12, 16):
        GPIO
    GPIO.output(row[0], 1)
    GPIO.output(row[3], 1
    for k in range 1000):

    sleep(0.5)
    GPIO.output(row[0], 0)
    GPIO.output(row[3], 0)
    GPIO.output(row[1], 1)
    GPIO.output(row[2], 1)
    sleep(0.5)
print("done")
GPIO.cleanup()