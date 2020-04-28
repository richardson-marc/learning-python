#!/usr/bin/env python

pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862

digits = int(input('how many digits of pi to display?'))

print('{:.{}f}'.format(pi, digits))





