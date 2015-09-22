import re
import textminer.validator as v

def words(input):
    return v.words(input)

def phone_number(input):
    if v.phone_number(input):
        raw = re.sub(r'[^0-9]', '', input)
        return {"area_code" : raw[:3], "number" : raw[3:6]+'-'+raw[6:]}

def money(input):
    if v.money(input):
        raw = re.sub(r'[\,]', '', input)
        return {"currency" : raw[0], "amount" : float(raw[1:])}

def zipcode(input):
    if v.zipcode(input):
        if len(input) < 6:
            return {"zip": input[:5], "plus4": None}
        else:
            return {"zip": input[:5], "plus4": input[6:]}
