#!/usr/bin/python3

for num in range(0, 100):
    if num == 99:
        print("{}".format("%02d" % (num)))
    else:
        print("{}".format("%02d" % (num)), end=", ")
