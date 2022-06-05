#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    print("{:d} {:s}{:s}".format(ln - 1,
                                 "argument" if ln <= 2 else "arguments",
                                 "." if ln == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
