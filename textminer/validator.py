import re


def binary(st):
    return re.match('^(0|1)+$', st)
