#!/usr/bin/python3
for a in range(25, -1, -1):
    if a % 2 != 0:
        print(chr(ord('a') + a), end='')
    else:
        print(chr(ord('A') + a), end='')
