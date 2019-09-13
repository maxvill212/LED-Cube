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
#Shortcut
out = GPIO.output

# Clean pins
def cleanup():
    out.cleanup()


#1 corner dot into full cube
#choose random dot on top level and then make it come down
#Random dots anywhere

#This resets all the pins
def reset():
    for i in range(16):
        out(column[i], 1)
    for i in range(4):
        out(row[i], 0)



#Grows squarre from top right down
for j in range(4):
    GPIO.output(column[j], 0)
    GPIO.output(column[j+12], 0)
    GPIO.output(row[j], 1)
    sleep(0.5)





#Top/Bottom, then mid, repead
for i in range(3):
    for j in range(16):
        GPIO.output(column[j], 0)
    GPIO.output(row[1], 0)
    GPIO.output(row[2], 0)
    GPIO.output(row[0], 1)
    GPIO.output(row[3], 1)
    sleep(0.5)
    GPIO.output(row[0], 0)
    GPIO.output(row[3], 0)
    GPIO.output(row[1], 1)
    GPIO.output(row[2], 1)
    sleep(0.5)





        #Outer shell, then core
#This resets all the pins
def reset():
    for i in range(16):
        GPIO.output(column[i], 1)
    for i in range(4):
        GPIO.output(row[i], 0)

#Lights the 4 walls
def verticalWalls():
    for i in range(4):
        GPIO.output(row[i], 1)
    for i in range(4):
        GPIO.output(column[i], 0)
    for i in range(12, 16, 1):
        GPIO.output(column[i], 0)
    for i in range(4, 9, 4):
        GPIO.output(column[i], 0)
    for i in range(7, 12, 4):
        GPIO.output(column[i], 0)

#Lights up the white LEDs in the middle
def middleTopBottomLEDs():
    for i in range(0, 4, 3):
        GPIO.output(row[i], 1)
    GPIO.output(column[5], 0)
    GPIO.output(column[6], 0)
    GPIO.output(column[9], 0)
    GPIO.output(column[10], 0)

#Lights up the blue LEDS
def middleLED():
    for i in range(1, 3, 1):
        GPIO.output(row[i], 1)
    GPIO.output(column[5], 0)
    GPIO.output(column[6], 0)
    GPIO.output(column[9], 0)
    GPIO.output(column[10], 0)

#The loop with the completed pattern
for i in range(3):
    for j in range(60):
        reset()
        verticalWalls()
        sleep(0.01)
        reset()
        middleTopBottomLEDs()
        sleep(0.01)
    reset()
    middleLED()
    sleep(1)





#This makes rain at random points on the grid
for i in range(15):
    reset()
    GPIO.output(random.choice(column), 0)
    for i in range(4):
        GPIO.output(row[i], 1)
        sleep(0.2)
        GPIO.output(row[i], 0)

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