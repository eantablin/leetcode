def strongPasswordChecker(self, password: str) -> int:
    lenCheck = False
    lowerC, upperC = False, False
    numeral = False
    
    numChanges = 0

    while lenCheck != True and lowerC != True and upperC != True and numeral != True:
        passLen = len(password)
        if passLen >= 6 and passLen <= 20:
            lenCheck = True # Passes length test
            
            for i in password:
                if i.isLower():
                    lowerC = True
                if i.isUpper():
                    upperC = True
                try:
                    i = int(i)
                    numeral = True
                except ValueError: # Not an integer
                    pass
                
        elif passLen < 6:
            while passLen < 6:
                passLen +=
            for i in 
        
        elif passLen > 20:
            password = password[:20:]