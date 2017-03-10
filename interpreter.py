import arithmetic
def interpret(expression):
    elementList = []
    for i in expression:
        elementList.append(i)
    isNumber = False
    symbolList = []
    allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for i in range(len(elementList)):
        for j in allowedChars:
            if str(j)==elementList[i]:
                isNumber = True
        if isNumber ==  False:
            symbolList.append(i)
        isNumber = False
    print(symbolList)
    if symbolList[len(symbolList)] == len
interpret("5^2*21+4^3/2.9")