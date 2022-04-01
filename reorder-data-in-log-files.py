from typing import List


def reorder(logs: List[str]):
    letters = []
    numbers = []

    for log in logs:

        if log.split(" ")[1][0].isdigit():
            numbers.append(log)
        else:
            letters.append(log)
 
    letters.sort(key= lambda i: (i.split(" ")[1:], i.split(" ")[0])) 

    return letters + numbers


def reorderLogFiles(logs: List[str]) -> List[str]:

    def get_key(log):
        _id, restOfLog = log.split(" ", maxsplit=1)
        return (0, restOfLog, _id) if restOfLog[0].isalpha() else (1, )

    return sorted(logs, key=get_key)

print(reorder(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(reorder(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

for i, c in enumerate("hello world"):
    print(i, c)