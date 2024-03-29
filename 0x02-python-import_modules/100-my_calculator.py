#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    ops = "+-*/"
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]

    if (op == '+'):
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif (op == '-'):
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif (op == '*'):
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    else:
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
