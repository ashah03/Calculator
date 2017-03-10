import arithmetic
def interpret(expression):
    elementList = []
    for i in expression:
        elementList.append(i)
    isNumber = False
    symbolList = []
    for i in range(len(elementList)):
        for j in range(9):
            if j==elementList[i]:
                isNumber = True
        if isNumber == True:
            symbolList.append(elementList[i])
    print(symbolList)
interpret("5^2*21+4^3/29")