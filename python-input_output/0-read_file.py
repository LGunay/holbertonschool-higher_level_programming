#!/usr/bin/python3
'''Read files'''


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        f.close()
