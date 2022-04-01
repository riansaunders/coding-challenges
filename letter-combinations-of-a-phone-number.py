def combos(digits):
    mapping = {
         "2": "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz",
     }
    res = []

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return

        letters = mapping[digits[i]] 
        for letter in letters:
            backtrack(i + 1, curStr + letter)


    if digits:
        backtrack(0, "")
    return res

print(combos("23"))
