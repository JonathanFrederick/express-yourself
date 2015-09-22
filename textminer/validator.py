import re




def binary(st):
    return re.match('^(0|1)+$', st)

def binary_even(st):
    return re.match('^(0|1)+0$', st)

def hex(st):
    return re.match('^[0-9A-F]+$', st)

def word(st):
    return re.match('^[0-9a-zA-Z-]*[a-zA-Z]$', st)

def words(st, count=None):
    new_st = re.split('\s+', st)
    if None in [word(w) for w in new_st]:
        return False
    else:
        if count:
            return count == len(new_st)
        else:
            return True

def phone_number(num):
    return re.match('^\(?[0-9]{3}\)?[. -]?[0-9]{3}[-.]?[0-9]{4}$', num)
