def identifyCoeffs(function):
    isZero = False
    if function.find("^") > 0:
        elementList = function.split("^") #Split at power symbol if one exists
        exPower = float(elementList[1])  # Save old power
    else:
        elementList = [function]
        exPower = 1
    new = []
    for i in elementList[0]: #Make a list out of the first term
        new += i
    if "x" in new:
        indX = new.index("x") #Find index of x
    else:
        indX = -1
    if indX > 0:
        oldCoeff = ""
        for i in range(len(new)-1):
            oldCoeff += new[i] #Identify the old coefficient: everything before x
        if oldCoeff == "-":
            oldCoeff = "-1"
        oldCoeff = float(oldCoeff)
    elif indX == 0:
        oldCoeff = 1
    elif type(function) == float or type(function) == int:
        isZero = True
    return oldCoeff, exPower, isZero

def derivative_axton(function):
    oldCoeff, exPower, isZero = identifyCoeffs(function)
   # else:
    #    return 0
    newCoeff = oldCoeff * exPower #Identify the new coefficient: the old coefficient times the old power
    newPower = exPower - 1 #Reduce the power by one
    newFunction = (str(newCoeff) + "x^" + str(newPower))  #Make the function into string form
    for i in newFunction: #Simplify x^0 to nothing and x^1 to x
        if newCoeff == 0:
            return 0
        if newPower == 0.0:
            return newCoeff
    return newFunction
#print(derivative_axton(input("Enter a function: ")))


def integral_axton(function):
    if function.find("^") > 0:
        elementList = function.split("^") #Split at power symbol if there is one
        exPower = float(elementList[1])  # Save old power
    else:
        elementList = [function]
        exPower = 1
    new = []
    for i in elementList[0]: #Make a list out of the first term
        new += i
    if "x" in new:
        indX = new.index("x") #Find index of x
    else:
        indX = -1
    if indX > 0:
        oldCoeff = ""
        for i in range(len(new)-1):
            oldCoeff += new[i] #Identify the old coefficient: everything before x
        oldCoeff = float(oldCoeff)
    elif indX == 0:
        oldCoeff = 1
    else:
        return 0
    newCoeff = oldCoeff / (exPower + 1)
    newPower = exPower + 1
    newFunction = str(newCoeff) + "x^" + str(newPower)

    if newPower == 1:
        newFunction == str(newCoeff) + "x"
    return newFunction


print(derivative_axton(input("Enter a function in the from of axton")))