#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("0 arguments.")
    elif len_arg == 2:
        print('{} argument:'.format(len_arg - 1))
    else:
        print('{} arguments:'.format(len_arg - 1))

    for i in range(1, len_arg):
        print('{}: {}'.format(i, sys.argv[i]))
