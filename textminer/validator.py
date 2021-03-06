import re




def binary(st):
    return re.match(r'^(0|1)+$', st)

def binary_even(st):
    return re.match(r'^(0|1)+0$', st)

def hex(st):
    return re.match(r'^[0-9A-F]+$', st)

def word(st):
    return re.match(r'^[0-9a-zA-Z-]*[a-zA-Z]$', st)

def words(st, count=None):
    new_st = re.split(r'\s+', st)
    if None in [word(w) for w in new_st]:
        return None
    else:
        if count:
            return count == len(new_st)
        else:
            return new_st

def phone_number(num):
    return re.match(r'^\(?[0-9]{3}\)?[. -]?[0-9]{3}[-.]?[0-9]{4}$', num)

def money(num):
    return re.match(r'^\$([0-9]+(,[0-9]{3})*)(\.[0-9]{2})?$', num)

def zipcode(num):
    return re.match(r'^[0-9]{5}(-[0-9]{4})?$', num)

def date(num):
    return re.match(r'^[0-9]{1,4}[/-][0-9]{1,2}[/-][0-9]{2,4}$', num)
