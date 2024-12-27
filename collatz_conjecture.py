
def collatz(num, loop):
    
    if num == 1: return loop
    
    elif loop == 500: return -1
    
    elif num == 1 and loop >0:
        return loop
    
    if num % 2 == 0:
         return collatz(num/2, loop+1)
    elif num % 2 == 1:
         return collatz(num*3 +1, loop+1)
        
n = 626331
print(collatz(n, 0))