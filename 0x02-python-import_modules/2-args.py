#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    cnt = len(sys.argv) - 1

    if cnt == 1:
        print("{} argument:\n{}: {}".format(cnt, cnt, sys.argv[cnt]))
    else:
        if cnt == 0:
            print("{} arguments.".format(cnt))
        else:
            print("{} arguments:".format(cnt))

            for i in range(cnt):
                print("{}: {}".format(i + 1, sys.argv[i + 1]))
