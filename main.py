# Import patterns and all other functions
from patterns import *

# Main program
reset()
for i in range(10):
    grow2d(1, 0.08)
    shrink2d(1, 0.08)
rain(5, 0.2)
scanner(4, 0.5)
cleanup()
