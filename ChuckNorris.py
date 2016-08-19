import sys
import functools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
import binascii

message = ""
message = message.join("{0:07b}".format(ord(i)) for i in input())


print(message, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
