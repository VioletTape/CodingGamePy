import sys
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = str(input()).upper()
pattern = []
for i in range(h):
    pattern.append(input())
print("A " + str(ord('A')), file=sys.stderr)
for i in range(h):
    for c in (j for j in t if j.isalpha() else '?'):
        l_offset = ord(t[c]) - 65
        if not t[c].isalpha():
            l_offset = 26
        # print("offset " + str(l_offset), file=sys.stderr)
        if l_offset < 0 or l_offset > 26:
            l_offset = 26
        print(pattern[i][l_offset*l:l_offset*l+l])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)