#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operator = {
        "+": add(int(argv[1]), int(argv[3])),
        "-": sub(int(argv[1]), int(argv[3])),
        '*': mul(int(argv[1]), int(argv[3])),
        "/": div(int(argv[1]), int(argv[3]))
        }
    resultado = operator.get(argv[2], "error")
    if resultado == "error":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], resultado))
