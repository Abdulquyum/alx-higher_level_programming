#!/usr/bin/python3
for i in range(0, 10):
    for q in range(0, 10):
        print(f"{i}{q}", end='')
        if i != 9 and q != 9:
            print(',', end=' ')
