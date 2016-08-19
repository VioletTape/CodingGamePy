import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = [int(t) for t in (input() or '0').split()]  # the n temperatures expressed as integers ranging from -273 to 5526
res = sorted(sorted(temp, reverse=True), key=lambda x: abs(x))[0]
print(res)



