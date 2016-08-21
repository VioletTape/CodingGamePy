import sys
import math
from collections import namedtuple

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

directionX = light_x - initial_tx
directionY = light_y - initial_ty
print("%i %i" % (directionX, directionY), file=sys.stderr)

direction = ""

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction = ""

    if directionY > 0:
        directionY -= 1
        direction = "S"

    if directionY < 0:
        directionY += 0
        direction = "N"

    if directionX > 0:
        directionX -= 1
        direction += "E"

    if directionX < 0:
        directionX += 1
        direction += "W"

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
