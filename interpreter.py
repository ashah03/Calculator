import arithmetic
import itertools
def interpret(expression):
    elementList = []
    for i in expression:
        elementList.append(i) #List of all elements in the expression
    isNumber = False
    symbolList = [] #List of symbol indexes in the string
    allowedNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    allowedSymbols = ["+", "-", "*", "/", "^", "(", ")", "."]
    for i in range(len(elementList)):
        if elementList[i] not in allowedNums + allowedSymbols:
            return "Error: Symbol not allowed"
        for j in allowedNums:
            if str(j)==elementList[i]:
                isNumber = True
        if isNumber ==  False:
            symbolList.append(i)
        isNumber = False
    print(symbolList)

    """lastChar = elementList[len(elementList) - 1]
    firstChar = elementList[0]
    if lastChar in allowedSymbols or firstChar in allowedSymbols:
         if lastChar != ")" and firstChar != "(":
            return("Error: Incorrect symbol positioning.")"""
print(interpret("(5^2*21+4^3/2.9"))

