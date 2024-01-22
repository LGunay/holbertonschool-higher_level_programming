#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            s = chr(ord(i) - 32)
        else:
            s = i
        print("{}".format(s), end="")
    print("")
