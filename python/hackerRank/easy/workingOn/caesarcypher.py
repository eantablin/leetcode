# s = "There's-a-starman-in-the-sky"
s = "Julius, there's a message in a bottle found in the waters of the Tigris. Return promptly."
k = 3


def caesarCypher(s, shift):
    dictionary = "abcdefghijklmnopqrstuvwxyz"
    upperDictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pHolder = retstring = ""
    lendict = len(dictionary)
    

    for i in range(lendict):
        total = i + shift

        if total >= lendict:
            pHolder += dictionary[total - lendict]
        else:
            pHolder += dictionary[total]


    for i in s:
        
        if i in upperDictionary:
            retstring += pHolder[upperDictionary.index(i)].upper()

        elif i in dictionary:
            retstring += pHolder[dictionary.index(i)]
        
        else:
            retstring += i



    
    return retstring

print(caesarCypher(s,k))
