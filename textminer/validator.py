import re


def binary(st):
    return re.match('^(0|1)+$', st)

def binary_even(st):
    return re.match('^(0|1)+0$', st)

def hex(st):
    return re.match('^[0-9A-F]+$', st)
