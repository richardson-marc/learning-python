#!/usr/bin/env python

digit = int(input('what is the digit?'))
#print('digit is' +digit)
print('digit is {}'.format(digit))
while True:
    count = ''
    count += 1
    if (digit %2 ==0):
        newdigit = digit / 2
        print('newdigit is {}'.format(newdigit))
#        break
        if newdigit == 1.0:
            print ('it took this many steps'.format(count))
            break
        else:
            newdigit = (digit * 3) + 1
