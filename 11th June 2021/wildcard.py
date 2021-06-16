def isMatching(ptn,strr):
    if len(ptn) == 0 and len(strr) == 0:
        return True

    if len(ptn) > 1 and ptn[0] == '*' and len(strr) == 0:
        return False

    if (len(ptn) > 1 and ptn[0] == '?') or (len(ptn) != 0
        and len(strr) !=0 and ptn[0] == strr[0]):
        return isMatching(ptn[1:],strr[1:]);

    if len(ptn) !=0 and ptn[0] == '*':
        return isMatching(ptn[1:],strr) or isMatching(ptn,strr[1:])
    return False

strr = input("string: ")
ptn = input("pattern: ")


if isMatching(ptn, strr):
    print(strr)
    print("Match Found")
else:
    print("No Match found")