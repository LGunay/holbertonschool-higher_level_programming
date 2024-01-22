#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if i == 8 and j > i:
            print("{}{}".format(i, j))
        if j > i and i != 8:
            print("{}{}, ".format(i, j), end="")
