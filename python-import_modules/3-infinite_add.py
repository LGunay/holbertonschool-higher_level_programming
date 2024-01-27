#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    add = 0
    argc = len(argv) - 1
    if argc == 0:
        print('0')
    else:
        for i in range(argc):
            add = add + int(argv[i + 1])
        print("{}".format(add))
