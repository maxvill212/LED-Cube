import RPi.GPIO as gpio
from time import sleep
import random

#Using BCM standard
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#Initializing as output
#Order on LED left to right, front (close to wire out) to back
#Cathode leads
gpio.setup([14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22], gpio.OUT, initial=gpio.HIGH)
#Anode Leads, top to bottom)
gpio.setup([5, 6, 13, 19], gpio.OUT, initial=gpio.LOW)

#Declaring columns and rows
column = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22]
row = [5, 6, 13, 19]

#Shortcut
out = gpio.output

#This resets all the pins
def reset():
    for i in range(16):
        out(column[i], 1)
    for i in range(4):
        out(row[i], 0)

# Clean pins
def cleanup():
   gpio.cleanup()

# Grows squarre from top right down
def grow2d(cyc):
    for i in range(cyc):
        for j in range(4):
            out(column[j], 0)
            out(column[j+12], 0)
            out(row[j], 1)
            sleep(0.5)

# Opposite of grow()
def shrink2d(cyc):
        for j in range(4):
            out(column[j], 0)
            out(column[j+12], 0)
            out(row[j], 1)
        for j in range(4):
            out(column[3-j], 1)
            out(column[15-j], 1)
            out(row[3-j], 0)
            sleep(0.5)

# Rain at random points on the grid
# cyc in the input from user for how many cycles
def rain(cyc):
    for i in range(cyc):
        reset()
        out(random.choice(column), 0)
        for j in range(4):
            out(row[j], 1)
            sleep(0.2)
            out(row[j], 0)

