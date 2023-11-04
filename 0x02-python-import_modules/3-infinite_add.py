#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    lenArgv = len(sys.argv) - 1

    if lenArgv == 0:
        print("0")
    else:
        sumAll = 0
        for cnt in range(lenArgv):
            sumAll += int(sys.argv[cnt + 1])
        print("{}".format(sumAll))
