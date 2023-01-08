import os
import sys
import subprocess

from math import *
print()
print()
print("List of operators:\n+ for addition\n- for subtraction\n/ for division\nx for multiplication\n|| for absolute value\nsqrt for square root\n^ for powers\n ")
num1 = float(input("Enter a number: "))
op = input("Choose an operator: ")
num2 = float(input("Enter another number (enter 0 if only need one value): "))
if op == "+":
    print(num1 + num2)
elif op == "/":
    print(num1 / num2)
elif op == "x":
    print(num1 * num2)
elif op == "||":
    print(abs(num1))
elif op == "-":
    print(num1 - num2)
elif op == "^":
    print(pow(num1,num2))
elif op == "sqrt":
    print(sqrt(num1))
else:
    print("We do not support the " + op + " operator")

subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
#code to restart the program