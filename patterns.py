
# cyc is the amount of cycles the user inputs
# spd is the duration of sleep by user input

# <editor-fold desc="Imports">
import RPi.GPIO as gpio
from time import sleep
import random
# </editor-fold>

# <editor-fold desc="Setup">
# Using BCM standard
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Initializing as output
# Order on LED left to right, front (close to wire out) to back
# Cathode leads
gpio.setup([14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22], gpio.OUT, initial=gpio.HIGH)
# Anode Leads, top to bottom)
gpio.setup([5, 6, 13, 19], gpio.OUT, initial=gpio.LOW)

# Declaring columns and rows
column = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 4, 17, 27, 22]
row = [5, 6, 13, 19]

# Shortcut
out = gpio.output
# </editor-fold>


# <editor-fold desc="Reset Pins"
# This resets all the pins
def reset():
    for i in range(16):
        out(column[i], 1)
    for i in range(4):
        out(row[i], 0)
# </editor-fold>


# <editor-fold desc="Clean Pins"""
# Clean pins
def cleanup():
    gpio.cleanup()
# </editor-fold>


# <editor-fold desc="2D Grow">
# Grows square from top right down
def grow2d(cyc, spd):
    for i in range(cyc):
        for j in range(4):
            out(column[j], 0)
            out(column[j + 12], 0)
            out(row[j], 1)
            sleep(spd)
# </editor-fold>


# <editor-fold desc="2D Shrink">
# Opposite of grow()
def shrink2d(cyc, spd):
    for i in range(cyc):
        for j in range(4):
            out(column[j], 0)
            out(column[j + 12], 0)
            out(row[j], 1)
        for j in range(3):
            out(column[3 - j], 1)
            out(column[15 - j], 1)
            out(row[3 - j], 0)
            sleep(spd)
# </editor-fold>


# <editor-fold desc="Rain">
# Rain at random points on the grid
# cyc in the input from user for how many cycles
def rain(cyc, spd):
    for i in range(cyc):
        reset()
        out(random.choice(column), 0)
        for j in range(4):
            out(row[j], 1)
            sleep(spd)
            out(row[j], 0)
# </editor-fold>


# <editor-fold desc="Top/down Scanner">
# Top and Bottom layer light up, then 2 middle
# spd is the speed at which the square grows
def scanner(cyc, spd):
    for i in range(cyc):
        for j in range(16):
            out(column[j], 0)
        out(row[1], 0)
        out(row[2], 0)
        out(row[0], 1)
        out(row[3], 1)
        sleep(spd)
        out(row[0], 0)
        out(row[3], 0)
        out(row[1], 1)
        out(row[2], 1)
        sleep(spd)
# </editor-fold>
