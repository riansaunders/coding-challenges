def happyNumber(n):

    path = set()
    
    def doMath(n):
        if n == 1:
            return True 

        if n in path:
            return False

        path.add(n)
        # digits = [int(digit) for digit in str(n)]
        # sum = 0
        # for digit in digits:
        #     sum += digit * digit

        # This is a fancy shortcut.
        total = sum([int(digit)**2 for digit in str(n)])

        return doMath(total)
        
    return doMath(n)        



print(happyNumber(19))
print(happyNumber(2))