import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    ms = []
    for i in range(8):
        ms.append(int(input()))
        # mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.

    # ms.index(max(ms))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The number of the mountain to fire on.
    print(ms.index(max(ms)))
