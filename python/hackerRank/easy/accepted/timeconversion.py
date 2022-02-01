s = "01:01:00AM"

def timeConversion(s):
    if "PM" in s and "12" not in s: # If it's after midday, add a 12
        s = str(12 + int(s[:2])) + s[2:]
    elif "AM" in s and "12" in s: # Special 00 case
        s = "00" + s[2:]
        
    return s[:-2] # Remove AM/PM from ending on all usecases

print(timeConversion(s))