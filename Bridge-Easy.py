import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

targetSpeed = gap + 1

slowAt = road + gap + (platform - sum(range(targetSpeed+1)) + 1)
print("Slow at %i; Gap is %i" % (slowAt, gap), file=sys.stderr)

jumped = 0


def before_jump():
    if coord_x < road and speed < targetSpeed:
        print("SPEED")
        return 0

    if coord_x < road and speed > targetSpeed:
        print("SLOW")
        return 0

    if coord_x < road-1 and speed == targetSpeed:
        print("WAIT")
        return 0

    if coord_x == road-1:
        print("JUMP")
        return 1 # jumped


def after_jump():
    if coord_x >= slowAt:
        print("SLOW")

    if coord_x < slowAt:
        print("WAIT")

    return 1

# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    if jumped == 0:
        jumped = before_jump()
    else:
        jumped = after_jump()

