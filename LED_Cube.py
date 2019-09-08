import RPi.GPIO as GPIO
from time import sleep
import random

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
#Shotcut
out = GPIO.output


#1 corner dot into full cube
#choose random dot on top level and then make it come down
#Random dots anywhere

#This resets all the pins
def reset():
    for i in range(16):
        out(column[i], 1)
    for i in range(4):
        out(row[i], 0)

#This drop in the core then moves up the sides, which slows down when coming up
def sides():
    reset()
    for i in range(4):
        out(column[i], 0)
    for i in range(12, 16):
        out(column[i], 0)
    for i in range(4, 8, 3):
        out(column[i], 0)
    for i in range(8, 12, 3):
        out(column[i], 0)


for i in range(10):
    reset()
    for i in range(4):
        out(row[i], 1)
        out(column[5], 0)
        out(column[6], 0)
        out(column[9], 0)
        out(column[10], 0)
        sleep(0.1)
        out(row[i], 0)

    sides()
    out(row[3], 1)
    sleep(0.1)
    out(row[2], 1)
    out(row[3], 0)
    sleep(0.2)
    out(row[1], 1)
    out(row[2], 0)
    sleep(0.3)
    out(row[0], 1)
    out(row[1], 0)
    sleep(0.2)
    for i in range (16):
        out(column[i], 0)
    sleep(0.1)


print("done")
GPIO.cleanup()