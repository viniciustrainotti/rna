#!/usr/bin/python
import math, sys

x1 = int(sys.argv[1])
x2 = int(sys.argv[2])
# x1, x2 = -3, 1

inputN1 = x1 * 0.2 + x2 * 0.8 + 1 * 0.1
inputN2 = x1 * 0.1 + x2 * 0.2 + 1 * 0.4
inputN3 = x1 * 0.9 + x2 * 0.5 + 1 * 0.2

print(inputN1, inputN2, inputN3)

inputN4 = inputN1 * 0.9 + inputN2 * 0.3 + inputN3 * 0.3 + 1 * 0.1

print(math.tanh(inputN4))
