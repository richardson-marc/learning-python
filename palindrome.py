#!/usr/bin/env python

def palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

