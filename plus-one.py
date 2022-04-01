def pone(digits):

    x = int("".join([ str(digits[i]) for i in range(len(digits))] )) + 1
    
    # The not lazy way to do it is increment the last digit by 1 and any forward digits by 1 that are also 9.

    return [ int(c) for c in str(x) ]

def pf(digits):
    digits = digits[::-1]
    carry, i = 1, 0
    while carry:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                carry = 0
        else:
            digits.append(1)
            return digits[::-1]
        i += 1

    return digits[::-1]

# print(pone([1,2,3]))
# print(pf([1,2,9,9]))
# print(pf([9,9,9,9]))
print(pf([1,2,9,9]))
print(pf([1,2,0,9]))
print(pf([9])) 