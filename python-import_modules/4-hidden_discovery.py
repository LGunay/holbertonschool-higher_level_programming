#!/usr/bin/python3

if __name__ == "__main__":
    import  hidden_4
    string = dir(hidden_4)
    for i in string:
        if i.startswith("__") == False:
            print("{}".format(i))
