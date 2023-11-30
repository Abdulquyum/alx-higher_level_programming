#!/usr/bin/pyhton3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        popped = str[:n] + str[n+1:]
        return popped
    else:
        return str
