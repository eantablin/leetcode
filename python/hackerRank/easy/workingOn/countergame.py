n = 132

def counterGame(n):
    
    starter = True # Switches between each on turn
    # If true is returned Richard wins, False Louise wins
    while n != 1:
        if n % 2 == 0:
            n //= 2
            starter = not starter
        else:
            n -= 1
    
    return "Richard" if starter else "Louise"

print(counterGame(n))