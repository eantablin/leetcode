s = "We promptly judged antique ivory buckles for the next prize"

def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetComplete = alphabet + alphabet.upper()
    
    pHolder = ""

    
    for i in s:
        if i in alphabetComplete:
            pHolder += i
            
    pHolder = pHolder.replace(" ", "")
    pHolder = pHolder.lower()
    pHolder = sorted(pHolder)
    pHolder = "".join(pHolder)

    for i in pHolder:
        if i in alphabet:
            alphabet = alphabet.replace(i, "")
    
    if len(alphabet) == 0:
        return "pangram"

    return "not pangram"

print(pangrams(s))